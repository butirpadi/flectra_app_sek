# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from pprint import pprint
from datetime import datetime


class BarangMove(models.Model):
    _name = 'inventaris.barang.move'
    
    barang_id = fields.Many2one('inventaris.barang', required=True, ondelete="cascade")
    lokasi_id = fields.Many2one('inventaris.lokasi', required=True, ondelete="restrict")
    move_date = fields.Datetime('Move Date', default=datetime.now())
    qty = fields.Integer('Quantity', default=1)
    active = fields.Boolean('Active', default=True)
    
    code = fields.Char(related="barang_id.code", string="System Code")
    serial_number = fields.Char(related="barang_id.serial_number", string="Serial Number")
    internal_reference = fields.Char(related="barang_id.internal_reference", string="Internal Reference")
    kategori_id = fields.Many2one('inventaris.kategori', string="Kategori", related="barang_id.kategori_id") 