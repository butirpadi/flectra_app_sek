# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
# from datetime import datetime as
import datetime


class Rppm(models.Model):
    _name = 'siswa.rppm'

    name = fields.Char(string='Ref#', requred=True, default='New')
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Ajaran', required=True,
                                     default=lambda x: x.env['siswa_ocb11.tahunajaran'].search([('active', '=', True)]))
    jenjang_id = fields.Many2one(
        'siswa_ocb11.jenjang', string="Kelompok", required=True)
    tema_id = fields.Many2one('siswa.tema',string="Tema")
    tema = fields.Char('Tema', required=True)
    subtema = fields.Char('Subtema')
    periode_awal = fields.Date('Periode Awal', required=True)
    periode_akhir = fields.Date('Periode Akhir', required=True)
    periode_str = fields.Char('Periode')
    employee_id = fields.Many2one(
        'hr.employee', string="Person", default=lambda self: self.get_employee())
    job_id = fields.Many2one(string=u'Job Position', comodel_name='hr.job',
                             ondelete='restrict', related="employee_id.job_id")
    tanggal = fields.Date('Tanggal', required=True,
                          default=datetime.datetime.today().date())
    state = fields.Selection([('reject', 'Reject'), ('draft', 'Draft'), ('post', 'Posted'), ('first', 'Confirmed'), (
        'second', 'Second Confirmed'), ('done', 'Done')], string='State', required=True, default='draft')
    semester = fields.Selection([('ganjil', 'Semester 1'), ('genap', 'Semester 2')],
                                string='Semester', required=True, default='ganjil')
    materi = fields.Text(string=u'Materi')
    desc = fields.Html('Catatan')
    kompetensi_dasar_ids = fields.Many2many(
        string=u'Kompetensi Dasar',
        comodel_name='kompetensi.dasar',
        relation='rppm_kompetensi_dasar_rel',
        column1='rppm_id',
        column2='kompetensi_dasar_id'
    )
    muatan_materi_ids = fields.One2many(
        string=u'Muatan Materi',
        comodel_name='rppm.muatan.materi.base.rel',
        inverse_name='rppm_id',
    )

    rppm_setting_id = fields.Many2one(
        string=u'RPPM Setting',
        comodel_name='rppm.setting',
        ondelete='restrict',
        default=lambda self: self.get_rppm_setting()
    )
    
    prosem_id = fields.Many2one(
        string=u'PROSEM',
        comodel_name='siswa.prosem',
        ondelete='restrict',
    )
    

    @api.multi
    def get_employee(self):
        emp = self.env['hr.employee'].search(
            [('user_id', '=', self.env.user.id)])
        return emp

    @api.model
    def get_rppm_action(self):
        # self.ensure_one()
        if self.env.user.has_group('siswa_kurikulum.kurikulum_manager'):
            print('Manager')
            action = self.env.ref(
                'siswa_kurikulum.siswa_rppm_manager_action_window').read()[0]
            # return self.env.ref('siswa_rppm_manager_action_window').window_action(self)
        elif self.env.user.has_group('siswa_kurikulum.kurikulum_guru'):
            print('Guru')
            action = self.env.ref(
                'siswa_kurikulum.siswa_rppm_action_window').read()[0]
            # return self.env.ref('siswa_rppm_action_window').window_action(self)

        # action =  self.env.ref('siswa_rppm_manager_action_window').window_action(self)
        # action = self.env.ref('siswa_kurikulum.siswa_rppm_manager_action_window').read()[0]
        return action
        # print('Inside get rppm action')

    @api.multi
    def action_reject(self):
        self.ensure_one()
        self.state = 'reject'
        print('Reject Application')

    @api.multi
    def get_rppm_setting(self):
        self.ensure_one
        # ta_aktif = self.env['siswa_ocb11.tahunajaran'].search(
        #     [('active', '=', True)])
        # rppm_set_id = self.env['rppm.setting'].search(
        #     [('tahunajaran_id', '=', ta_aktif.id)], limit=1)
        # get rppm setting yang aktif
        rppm_set_id = self.env['rppm.setting'].search(
            [('aktif', '=', True)], limit=1)
        return rppm_set_id

    @api.multi
    def action_print_view(self):
        self.ensure_one()
        return self.env.ref('siswa_kurikulum.rppm_report_action').report_action(self)

    @api.multi
    def action_first_confirm(self):
        for rec in self:
            self.state = 'first'

    @api.multi
    def action_second_confirm(self):
        for rec in self:
            print('second confirm')

    @api.multi
    def action_submit(self):
        for rec in self:
            # cek apakah datah telah diisi
            if rec.materi != "" and len(rec.kompetensi_dasar_ids) > 0 and len(rec.muatan_materi_ids) > 0:
                # update state
                rec.state = 'post'
            else:
                # alert error
                raise exceptions.ValidationError(
                    _('Submit form gagal, lengkapi data yang diperlukan.'))

    @api.multi
    def generate_muatan_materi(self):
        for rec in self:
            a_start = datetime.datetime.strptime(rec.periode_awal, '%Y-%m-%d')
            an_end = datetime.datetime.strptime(rec.periode_akhir, '%Y-%m-%d')
            delta = datetime.timedelta(days=1)

            # clear data lama
            rec.muatan_materi_ids.unlink()

            muatan_base = []
            while a_start <= an_end:
                new_data = (0, 0, {
                    'tanggal': a_start
                })
                muatan_base.append(new_data)
                a_start += delta
            rec.muatan_materi_ids = muatan_base
            # print('test')

            # new_date = new Date(rec.periode_awal.year,rec.periode_awal.month,rec.periode_awal.day)
            # print(type(rec.periode_awal))
            # print(type(dlta))

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(
                    force_company=vals['company_id']).next_by_code('siswa.rppm.sequence') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'siswa.rppm.sequence') or _('New')

        result = super(Rppm, self).create(vals)
        return result

    @api.multi
    def unlink(self):
        res = []
        for rec in self:
            if rec.state != 'draft':
                raise exceptions.except_orm(_('Warning'), _(
                    'You can not delete at this state.'))
            else:
                res.append(super(Rppm, self).unlink())

        return res