# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subtema(models.Model):
    _name = 'siswa.subtema'

    name = fields.Char('Nama', required=True)
    tema_id = fields.Many2one(
        string=u'Tema',
        comodel_name='siswa.tema',
        ondelete='cascade',
        required=True
    )
