# -*- coding: utf-8 -*-

from flectra import models, fields, api

class Color(models.Model):
    _name = 'inventaris.color'
    
    name = fields.Char('Name', required=True)  