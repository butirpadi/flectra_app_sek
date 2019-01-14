from odoo import models, fields, api, _


class SiswaSetting(models.Model):
    _name = 'siswa.setting'

    default_siswa_number = fields.Selection(
        [('nis', 'NIS'), ('induk', 'Nomor System')], string="Default Siswa ID Number", default="induk")
    report_logo = fields.Binary("Report Logo", attachment=True)

    def execute(self):
        self.write({
            'default_siswa_number': self.default_siswa_number
        })

        # set report_logo on res_company
        company_id = self.env.user.company_id
        company_id.report_logo = self.report_logo
