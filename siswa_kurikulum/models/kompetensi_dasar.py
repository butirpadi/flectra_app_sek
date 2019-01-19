# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KompetensiDasar(models.Model):
    _name = 'kompetensi.dasar'

    name = fields.Char('Kode', required=True)
    desc = fields.Text('Keterangan', required=True)
    kompetensi_inti_id = fields.Many2one(
        'kompetensi.inti', required=True, string="Kompetensi Inti")
