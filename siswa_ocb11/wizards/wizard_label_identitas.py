from odoo import models, fields, api
from pprint import pprint
from datetime import datetime


class WizardLabelIdentitas(models.TransientModel):
    _name = 'wizard.label.identitas'

    state = fields.Selection([('draft', 'Draft'), ('post', 'Posted')],
                             string='State', required=True, default='draft')
    tahunajaran_id = fields.Many2one(
        'siswa_ocb11.tahunajaran', string="Tahun Ajaran")
    rombel_ids = fields.Many2many(
        string=u'Rombongan Belajar',
        comodel_name='siswa_ocb11.rombel',
        relation='label_identitas_rombel_rel',
        column1='wizard_id',
        column2='rombel_id',
    )
    rombel_siswa_ids = fields.Many2many(
        string=u'Siswa',
        comodel_name='siswa_ocb11.rombel_siswa',
        relation='label_identitas_rombel_siswa_rel',
        column1='wizard_id',
        column2='rombel_siswa_id',
    )
    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.user.company_id.id)

    @api.multi
    def action_save(self):
        self.ensure_one()
        self.state = 'post'
        rbs_temp = []
        for rom in self.rombel_ids:
            rbs_ids = self.env['siswa_ocb11.rombel_siswa'].search(
                [('tahunajaran_id', '=', self.tahunajaran_id.id), ('rombel_id', '=', rom.id)])
            # rbs_temp.append(rbs_ids.ids)
            rbs_temp += rbs_ids.ids

        self.rombel_siswa_ids = [(6, None, rbs_temp)]
        # self.rombel_siswa_ids = [(6, None, rbs_ids.ids)

        return {
            'name': 'Label Identitas',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wizard.label.identitas',
            'target': 'current',
            'res_id': self.id,
            'type': 'ir.actions.act_window',
        }

    @api.multi
    def print_action(self):
        self.ensure_one()
        return self.env.ref('siswa_ocb11.report_label_identitas_action').report_action(self)
