# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tema(models.Model):
    _name = 'siswa.tema'

    name = fields.Char('Nama', required=True)