# -*- coding: utf-8 -*-

from flectra import models, fields, api


class SiswaSurat(models.Model):
    _name = 'siswa.surat'

    name = fields.Char('Name', required=True,
                       default="SURAT CONFIGURATION")
    title = fields.Char('Title', required=True)
    perihal = fields.Char('Perihal', required=True, default="")
    content_1 = fields.Html('Content 1')
    content_2 = fields.Html('Content 2')
    author_job = fields.Char('Author Position', required=True)
    author = fields.Char('Author', required=True)
    table_position = fields.Selection([('middle', 'Middle'), (
        'bottom', 'Bottom')], string='Table Position', required=True, default='middle')
    biaya_ids = fields.One2many(
        string=u'Default Biaya',
        comodel_name='surat.tagihan.biaya.rel',
        inverse_name='surat_id',
    )
    surat_tagihan_seq = fields.Integer('Sequence', default=1)
    surat_tagihan_prefix = fields.Char(
        'Prefix', default="ST", required=True)
