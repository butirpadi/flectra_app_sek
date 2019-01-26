from odoo import models, fields, api, exceptions, _
import datetime
from pprint import pprint


class Prosem(models.Model):
    _name = 'siswa.prosem'

    name = fields.Char('Ref#', required=True, copy=False, default="New")
    protah_id = fields.Many2one(
        string=u'PROTAH',
        comodel_name='siswa.protah',
        ondelete='restrict',
    )
    jenjang_id = fields.Many2one('siswa_ocb11.jenjang', related="protah_id.jenjang_id")
    employee_id = fields.Many2one('hr.employee', related="protah_id.employee_id")
    state = fields.Selection([('reject', 'Reject'), ('draft', 'Draft'), ('post', 'Posted'), ('first', 'Confirmed'), (
        'second', 'Second Confirmed'), ('done', 'Done')], string='State', required=True, default='draft')
    
    tahunajaran_id = fields.Many2one(
        string=u'Tahun Ajaran',
        comodel_name='siswa_ocb11.tahunajaran',
        ondelete='restrict',
    )
    
    semester = fields.Selection([('ganjil', 'Semester 1'), ('genap', 'Semester 2')],
                                string='Semester', required=True, default='ganjil')
    
    rppm_ids = fields.One2many(
        string=u'RPPM',
        comodel_name='siswa.rppm',
        inverse_name='prosem_id',
    )

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(
                    force_company=vals['company_id']).next_by_code('siswa.prosem.sequence') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'siswa.prosem.sequence') or _('New')

        result = super(Prosem, self).create(vals)
        return result
    
