# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SuratTagihanBiayaRel(models.Model):
    _name = 'surat.tagihan.biaya.rel'

    surat_id = fields.Many2one('siswa.surat', string='Surat', required=True)
    biaya_id = fields.Many2one('siswa_keu_ocb11.biaya', string="Biaya")
    is_bulanan = fields.Boolean(related="biaya_id.is_bulanan", string="Is Bulanan")
    bulan = fields.Selection([(0, 'Bulan'), 
                            (1, 'Januari'),
                            (2, 'Februari'),
                            (3, 'Maret'),
                            (4, 'April'),
                            (5, 'Mei'),
                            (6, 'Juni'),
                            (7, 'Juli'),
                            (8, 'Agustus'),
                            (9, 'September'),
                            (10, 'Oktober'),
                            (11, 'November'),
                            (12, 'Desember'),
                            ], string='Bulan')