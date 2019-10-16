from odoo import models, fields, api, _
from odoo.exceptions import UserError


class GolonganGaji(models.Model):
    _name = 'golongan.gaji'

    name = fields.Char(string='Nama', required=True, )
    active = fields.Boolean(default=True)
    batas_atas = fields.Monetary(string='Batas Atas')
    batas_bawah = fields.Monetary(string='Batas Bawah')
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    
    
    
