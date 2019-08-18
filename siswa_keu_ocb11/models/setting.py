from odoo import models, fields, api, _


class SiswaSetting(models.Model):
    _inherit = 'siswa.setting'

    default_income_account = fields.Many2one('account.account', string="Income Account")

    @api.multi
    def write(self, vals):
        
        if 'default_siswa_number' in vals:
            # update all about default siswa_id 
            self.env.cr.execute("update siswa_keu_ocb11_pembayaran set default_siswa_number = '" + vals['default_siswa_number'] + "'" )
        
        res = super(SiswaSetting, self).write(vals)
        
        return res 
