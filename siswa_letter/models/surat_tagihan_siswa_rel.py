# -*- coding: utf-8 -*-

from flectra import models, fields, api


class SuratTagihanSiswaRel(models.Model):
    _name = 'surat.tagihan.siswa.rel'

    name = fields.Char('Nomor Surat')
    wizard_id = fields.Many2one(
        'siswa.wizard.surat.tagihan', string='Surat', required=True, ondelete="cascade")
    siswa_id = fields.Many2one('res.partner', string="Siswa", required=True)
    active_rombel_id = fields.Many2one('siswa_ocb11.rombel', related="siswa_id.active_rombel_id", string="Rombongan Belajar")
    nis = fields.Char(related="siswa_id.nis", string="NIS")
    induk = fields.Char(related="siswa_id.induk", string="Siswa ID")
    default_siswa_number = fields.Selection([('nis', 'NIS'), ('induk', 'System Number')], string='Default Siswa Number', default=lambda self: self.env['siswa.setting'].search([],limit=1).default_siswa_number )
    total_tagihan = fields.Float('Total Tagihan', default=0.0)    
    tagihan_siswa_biaya_ids = fields.Many2many(
        string=u'Siswa Biaya',
        comodel_name='siswa_keu_ocb11.siswa_biaya',
        relation='surat_tagihan_siswa_biaya_rel',
        column1='surat_tagihan_siswa_rel_id',
        column2='siswa_biaya_id',
    )
    surat_id = fields.Many2one('siswa.surat', string="Surat")
    
