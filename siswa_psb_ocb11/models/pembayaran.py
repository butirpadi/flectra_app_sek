# -*- coding: utf-8 -*-

from flectra import models, fields, api, exceptions, _
from flectra.addons import decimal_precision as dp
from datetime import datetime
from pprint import pprint


class pembayaran(models.Model):
    _inherit = 'siswa_keu_ocb11.pembayaran'

    psb_reference_id = fields.Many2one('siswa_psb_ocb11.calon_siswa', string="PSB Reference")
    psb_reg_number = fields.Char(related="psb_reference_id.reg_number", string="PSB Reference")
    
    def get_psb_view(self):
        return {
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'siswa_psb_ocb11.calon_siswa',
                'target': 'current',
                'res_id' : self.psb_reference_id.id,
                'type': 'ir.actions.act_window',
            }
    
    def action_cancel(self):
        if self.psb_reference_id:
            raise exceptions.ValidationError(_('Cancel not allowed at this state.'))
        else:
            return super(pembayaran,self).action_cancel() 