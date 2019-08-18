from odoo import models, fields, api, _


class SiswaSetting(models.Model):
    _inherit = 'siswa.setting'

    default_tabungan_income_account = fields.Many2one('account.account', string="Default Tabungan Account")
    counterpart_tabungan_income_account = fields.Many2one('account.account', string="Counterpart Tabungan Account")
    default_tabungan_journal = fields.Many2one('account.journal', string="Tabungan Income Journal")

    @api.multi
    def write(self, vals):
        print('--------------- inside module tabungan ----------------------')
        
        if 'default_siswa_number' in vals:
            print(vals['default_siswa_number'])
            # update all about default siswa_id 
            self.env.cr.execute("update siswa_tab_ocb11_tabungan set default_siswa_number = '" + vals['default_siswa_number'] + "'" )
        
        res = super(SiswaSetting, self).write(vals)
        
        return res 
