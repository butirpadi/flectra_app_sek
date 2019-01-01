from odoo import models, fields, api, _


class SiswaSetting(models.Model):
    _name = 'siswa.setting'

    default_siswa_number = fields.Selection([('nis', 'NIS'), ('induk', 'Nomor System')], string="Default Siswa ID Number", default="induk")
    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.user.company_id.id)
    
    def execute(self):
        self.write({
                'default_siswa_number' : self.default_siswa_number
            })  