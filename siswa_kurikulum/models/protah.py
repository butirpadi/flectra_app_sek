# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import datetime


class Protah(models.Model):
    _name = 'siswa.protah'

    name = fields.Char('Ref#', required=True, default="New")
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
    state = fields.Selection([('reject', 'Reject'), ('draft', 'Draft'), ('post', 'Posted'), ('first', 'Confirmed'), (
        'second', 'Second Confirmed'), ('done', 'Done')], string='State', required=True, default='draft')

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
        print('submit form')
        self.state = 'post'

    @api.model
    def get_protah_action(self):
        # self.ensure_one()
        if self.env.user.has_group('siswa_kurikulum.kurikulum_manager'):
            print('Manager')
            action = self.env.ref(
                'siswa_kurikulum.siswa_protah_manager_action_window').read()[0]
        elif self.env.user.has_group('siswa_kurikulum.kurikulum_guru'):
            print('Guru')
            action = self.env.ref(
                'siswa_kurikulum.siswa_protah_action_window').read()[0]

        return action

    @api.multi
    def get_employee(self):
        emp = self.env['hr.employee'].search(
            [('user_id', '=', self.env.user.id)])
        return emp
