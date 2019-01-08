# -*- coding: utf-8 -*-

from flectra import models, fields, api

class Brand(models.Model):
    _name = 'inventaris.brand'
    
    name = fields.Char('Name', required=True)  