# -*- coding: utf-8 -*-

from flectra import models, fields, api

# class basic_install_ocb11(models.Model):
#     _name = 'basic_install_ocb11.basic_install_ocb11'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100 