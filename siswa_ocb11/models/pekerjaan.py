# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pekerjaan(models.Model):
    _name = 'siswa_ocb11.pekerjaan'

    name = fields.Char(string="Nama", required=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id)
     