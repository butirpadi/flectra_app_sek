# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SumberDana(models.Model):
    _name = 'inventaris.sumber.dana'
    
    name = fields.Char('Name', required=True)  