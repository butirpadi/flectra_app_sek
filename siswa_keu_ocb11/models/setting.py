from flectra import models, fields, api, _


class SiswaSetting(models.Model):
    _inherit = 'siswa.setting'

    @api.multi
    def write(self, vals):
        
        if 'default_siswa_number' in vals:
            # update all about default siswa_id 
            self.env.cr.execute("update siswa_keu_ocb11_pembayaran set default_siswa_number = '" + vals['default_siswa_number'] + "'" )
        
        res = super(SiswaSetting, self).write(vals)
        
        return res 
