# -*- coding: utf-8 -*-

from flectra import models, fields, api

class WizardSuratTagihanBiayaRel(models.Model):
    _name = 'wizard.surat.tagihan.biaya.rel'

    wizard_id = fields.Many2one('siswa.wizard.surat.tagihan', string='Wizard', ondelete="cascade")
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