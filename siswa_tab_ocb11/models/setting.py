from odoo import models, fields, api, _


class SiswaSetting(models.Model):
    _inherit = 'siswa.setting'

    @api.multi
    def write(self, vals):
        print('--------------- inside module tabungan ----------------------')
        
        if 'default_siswa_number' in vals:
            print(vals['default_siswa_number'])
            # update all about default siswa_id 
            self.env.cr.execute("update siswa_tab_ocb11_tabungan set default_siswa_number = '" + vals['default_siswa_number'] + "'" )
        
        res = super(SiswaSetting, self).write(vals)
        
        return res 
