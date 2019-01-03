# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class action_confirm(models.Model):
    _name = 'siswa_keu_ocb11.action_confirm'

    pembayaran_id = fields.Many2one('siswa_keu_ocb11.pembayaran', string='Pembayaran', ondelete='restrict')
    kas_id = fields.Many2one('siswa_keu_ocb11.kas', 'Kas', ondelete='restrict')
    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.user.company_id.id)
      