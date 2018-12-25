from odoo import models, fields, api
from pprint import pprint
from datetime import datetime


class WizardSuratTagihan(models.TransientModel):
    _name = 'siswa.wizard.surat.tagihan'

    name = fields.Char('name', default="Surat Tagihan")
    tahunajaran_id = fields.Many2one(
        'siswa_ocb11.tahunajaran', string="Tahun Ajaran")
    jenjang_ids = fields.Many2many('siswa_ocb11.jenjang', string="Jenjang")
    rombel_ids = fields.Many2many(
        'siswa_ocb11.rombel', string="Rombongan Belajar")
    siswa_ids = fields.Many2many('res.partner', string="Siswa", domain=[
                                 ('is_siswa', '=', True)])
