# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MuatanMateri(models.Model):
    _name = 'muatan.materi'

    name = fields.Char('Kode', required=True)
    desc = fields.Text('Keterangan', required=True)
    kategori_id = fields.Many2one(
        'kategori.muatan.materi', string="Kategori", required=True)
    kategori_code = fields.Char('Kode Kategori', related="kategori_id.code")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
