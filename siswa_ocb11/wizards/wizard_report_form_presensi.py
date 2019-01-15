from odoo import models, fields, api, _
from pprint import pprint
from datetime import datetime
import calendar


class wizard_report_form_presensi(models.TransientModel):
    _name = 'siswa_ocb11.wizard_report_form_presensi'

    name = fields.Char('Name', default='Report Kas')
    rombel_id = fields.Many2one(
        'siswa_ocb11.rombel', required=True, string='Rombongan Belajar', ondelete="cascade")
    siswa_ids = fields.Many2many('res.partner', relation='siswa_ocb11_report_form_presensi_siswa_rel',
                                 column1='report_id', column2='siswa_id', string="Data Siswa", ondelete="cascade")
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string="Tahun Ajaran", default=lambda self: self.env['siswa_ocb11.tahunajaran'].search([
                                     ('active', '=', True)]), required=True, ondelete="cascade")
    tanggal = fields.Date('Tanggal', required=True,
                          default=datetime.today().date())
    default_siswa_number = fields.Selection([('nis', 'NIS'), ('induk', 'System Number')], string='Default Siswa Number',
                                            default=lambda self: self.env['siswa.setting'].search([], limit=1).default_siswa_number)
    report_logo = fields.Binary("Report Logo", attachment=True)
    report_type = fields.Selection(
        [('daily', 'Harian'), ('monthly', 'Bulanan')], string='Tipe', default='daily', required=True)
    last_day = fields.Integer('Last Day', default=30)

    def action_save(self):
        self.ensure_one()
        # set kas_ids
        # siswas = self.env['res.partner'].search([('active_rombel_id','=',self.rombel_id.id)])
        siswas = self.env['siswa_ocb11.rombel_siswa'].search(
            [('tahunajaran_id', '=', self.tahunajaran_id.id), ('rombel_id', '=', self.rombel_id.id)])
        # get report logo
        setting_id = self.env.ref('siswa_ocb11.siswa_number_default_setting')
        self.report_logo = setting_id.report_logo

        # reg_sis = []
        for sis in siswas:
            self.write({
                'siswa_ids': [(4, sis.siswa_id.id)]
            })

        # get month range
        tanggal_str = datetime.strptime(self.tanggal,"%Y-%m-%d")
        self.last_day = calendar.monthrange(
            tanggal_str.year, tanggal_str.month)[1]
        
        if self.report_type == 'daily':
            return self.env.ref('siswa_ocb11.report_form_presensi_action').report_action(self)
        else:
            print('Monthly Report')
            print(self.last_day)
            return self.env.ref('siswa_ocb11.report_form_presensi_monthly_action').report_action(self)

