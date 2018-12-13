# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Satuan(models.Model):
    _name = 'inventaris.satuan'
    
    name = fields.Char('Name', required=True)  