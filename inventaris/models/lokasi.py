# -*- coding: utf-8 -*-

from flectra import models, fields, api

class Lokasi(models.Model):
    _name = 'inventaris.lokasi'
    
    name = fields.Char('Name', required=True)
    barang_move_ids = fields.One2many('inventaris.barang.move', inverse_name="lokasi_id", string="Aset Move")
