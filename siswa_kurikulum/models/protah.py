# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import datetime
from pprint import pprint


class Protah(models.Model):
    _name = 'siswa.protah'

    active = fields.Boolean('Active', default=True)
    kurikulum_setting_id = fields.Many2one(
        'kurikulum.setting', default=lambda self: self.env['kurikulum.setting'].search([], limit=1))
    name = fields.Char('Ref#', required=True, copy=False, default="New")
    tahunajaran_id = fields.Many2one(
        string=u'Tahun Ajaran',
        comodel_name='siswa_ocb11.tahunajaran',
        ondelete='restrict',
        required=True
    )

    jenjang_id = fields.Many2one(
        string=u'Jenjang',
        comodel_name='siswa_ocb11.jenjang',
        ondelete='restrict',
    )

    tanggal = fields.Date('Tanggal', required=True,
                          default=datetime.datetime.today().date())
    state = fields.Selection([('cancel', 'Cancelled'),('reject', 'Reject'), ('draft', 'Draft'), ('post', 'Posted'), ('first', 'Confirmed'), (
        'second', 'On Progress'), ('done', 'Done')], string='State', required=True, default='draft')

    prosem_ids = fields.One2many(
        string=u'PROSEM',
        comodel_name='siswa.prosem',
        inverse_name='protah_id',
    )

    employee_id = fields.Many2one(
        string=u'Person',
        comodel_name='hr.employee',
        ondelete='restrict',
        default=lambda self: self.get_employee()
    )

    job_id = fields.Many2one(
        string=u'Job Position',
        comodel_name='hr.job',
        ondelete='restrict',
        related="employee_id.job_id"
    )

    tema_ids = fields.One2many(
        string=u'Tema',
        comodel_name='protah.tema.rel',
        inverse_name='protah_id',
    )

    @api.multi
    def action_cancel(self):
        self.ensure_one()
        # cek user akses
        if self.env.user.id != self.employee_id.user_id.id:
            raise exceptions.ValidationError(
                _('You have no right to cancel this document.'))
        else:
            self.state = 'cancel'
            self.active = False

    @api.multi
    def action_set_to_draft(self):
        self.ensure_one()
        self.state = 'draft'

    @api.multi 
    def action_reject(self):
        self.state = 'reject'

    @api.multi
    def action_second_confirm(self):
        self.ensure_one()
        print('Post Confirm')
        self.state = 'second'
        self.generate_prosem()

    @api.multi
    def action_first_confirm(self):
        self.ensure_one()
        # cek confirmation level setting
        self.state = 'first'
        if self.kurikulum_setting_id.is_two_step_approval:
            # make two step approval
            print('Two Step Approval')
        else:
            self.state = 'second'
            # single step approval
            self.generate_prosem()

    @api.multi
    def generate_prosem(self):
        self.ensure_one()

        prosems = []
        # new_prosem_ganjil = self.env['siswa.prosem'].create({
        #     'tahunajaran_id': self.tahunajaran_id.id,
        #     'semester': 'ganjil'
        # })
        prosems.append((0, 0, {
            'name' : 'New',
            'tahunajaran_id': self.tahunajaran_id.id,
            'semester': 'ganjil'
        }))
        # new_prosem_genap = self.env['siswa.prosem'].create({
        #     'tahunajaran_id': self.tahunajaran_id.id,
        #     'semester': 'genap'
        # })
        prosems.append((0, 0, {
            'name' : 'New',
            'tahunajaran_id': self.tahunajaran_id.id,
            'semester': 'genap'
        }))

        self.prosem_ids = prosems

        # generate rppm for every prosem
        for prosm in self.prosem_ids:
            # get protah semester & tema
            protah_tema_ids = self.tema_ids.search([('semester','=',prosm.semester)])
            rppm_ids = []
            for tema in protah_tema_ids:
                rppm_ids.append((0,0,{
                    'tahunajaran_id' : self.tahunajaran_id.id,
                    'jenjang_id' : self.jenjang_id.id,
                    'tema_id' : tema.tema_id.id,
                    'tema' : tema.tema_id.name,
                    'periode_awal' : tema.periode_awal,
                    'periode_akhir' : tema.periode_akhir,
                    'employee_id' : self.employee_id.id,
                    'tanggal' : datetime.datetime.today().date(),
                    'semester' : prosm.semester
                }))
            prosm.rppm_ids = rppm_ids


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(
                    force_company=vals['company_id']).next_by_code('siswa.protah.sequence') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'siswa.protah.sequence') or _('New')

        result = super(Protah, self).create(vals)
        return result

    @api.multi
    def action_submit(self):
        self.ensure_one()
        # check rpp is available or no
        if self.tema_ids:
            print('submit form')
            self.state = 'post'
        else:
            raise exceptions.ValidationError(
                _('Submit form gagal, lengkapi data yang diperlukan.'))

    @api.model
    def get_protah_action(self):
        # set default action as guru
        action = self.env.ref(
            'siswa_kurikulum.siswa_protah_action_window').read()[0]

        # # get defauilt setting current
        # # self.ensure_one()
        kurr_sett = self.env['kurikulum.setting'].search([], limit=1)

        # pprint(kurr_sett)
        # self.kurikulum_setting_id = self.env['kurikulum.setting'].search([], limit=1)

        # self.kurikulum_setting_id = self.env['kurikulum.setting'].search(
        #     [], limit=1)
        # self.kurikulum_setting_id = kurr_sett[0].id

        if self.env.user.has_group('siswa_kurikulum.kurikulum_manager'):
            print('Manager')
            # set default action for manager
            action = self.env.ref(
                'siswa_kurikulum.siswa_protah_manager_action_window').read()[0]

            # check if two step approval
            print('is two step ? ' +
                  str(kurr_sett.is_two_step_approval))
            if kurr_sett.is_two_step_approval:
                print('Two Step Approval')
                # check if this user is as second approval
                # get self employee
                employee_me = self.env['hr.employee'].search(
                    [('user_id', '=', self.env.user.id)])

                if employee_me:
                    if employee_me.id == kurr_sett.second_approval_id.id:
                        print('Second step employee')
                        action = self.env.ref(
                            'siswa_kurikulum.siswa_protah_manager_two_level_action_window').read()[0]

        # # elif self.env.user.has_group('siswa_kurikulum.kurikulum_guru'):
        # #     print('Guru')
        # #     action = self.env.ref(
        # #         'siswa_kurikulum.siswa_protah_action_window').read()[0]

        if self.env.user.has_group('base.group_system'):
            action = self.env.ref(
                'siswa_kurikulum.siswa_protah_root_action_window').read()[0]

        return action

    @api.multi
    def get_employee(self):
        emp = self.env['hr.employee'].search(
            [('user_id', '=', self.env.user.id)])
        return emp
