# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProtahTemaRel(models.Model):
    _name = 'protah.tema.rel'

    name = fields.Char('Name', required=True, default="New")
    
    protah_id = fields.Many2one(
        string=u'Protah',
        comodel_name='siswa.protah',
        ondelete='cascade',
    )
    
    tema_id = fields.Many2one(
        string=u'Tema',
        comodel_name='siswa.tema',
        ondelete='restrict',
    )

    semester = fields.Selection([('ganjil', 'Semester 1'), ('genap', 'Semester 2')],
                                string='Semester', required=True, default='ganjil')
    periode_awal = fields.Date('Periode Awal', required=True)
    periode_akhir = fields.Date('Periode Akhir', required=True)
    
    