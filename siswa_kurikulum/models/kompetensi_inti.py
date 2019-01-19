# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KompetensiInti(models.Model):
    _name = 'kompetensi.inti'

    name = fields.Char('Kode', required=True)
    desc = fields.Text('Keterangan', required=True)
