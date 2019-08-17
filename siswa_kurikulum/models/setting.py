from odoo import models, fields, api, _


class SiswaSetting(models.Model):
    _inherit = 'siswa.setting'

    jumlah_hari_aktif = fields.Selection([(7, '7'), (6, '6'), (5, '5'), (4, '4'), (
        3, '3'), (2, '2')], string='Hari Aktif/Minggu', default=5)
    
    def execute(self):
        res = super(SiswaSetting,self).execute()
        self.write({
            'jumlah_hari_aktif': self.jumlah_hari_aktif
        })
        return res