# -*- coding: utf-8 -*-

from flectra import models, fields, api

# class siswa_letter(models.Model):
#     _name = 'siswa_letter.siswa_letter'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100