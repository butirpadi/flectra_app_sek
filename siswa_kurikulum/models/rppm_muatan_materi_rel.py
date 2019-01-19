# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RppmMuatanMateriRel(models.Model):
    _name = 'rppm.muatan.materi.rel'

    tanggal = fields.Date('Tanggal')
    
    base_id = fields.Many2one(
        string=u'Base',
        comodel_name='rppm.muatan.materi.base.rel',
        ondelete='cascade',
    )
    
    muatan_materi_ids = fields.Many2many(
        string=u'Muatan Materi',
        comodel_name='muatan.materi',
        relation='rppm_muatan_materi_detail_rel',
        column1='base_rel_id',
        column2='muatan_materi_id',
    )
    
    