# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RppmMuatanMateriBaseRel(models.Model):
    _name = 'rppm.muatan.materi.base.rel'

    tanggal = fields.Date('Tanggal')
    rppm_id = fields.Many2one(
        string=u'RPPM ID',
        comodel_name='model.name',
        ondelete='set null',
    )
    
    # rppm_muatan_materi_ids = fields.One2many(
    #     string=u'Muatan Materi',
    #     comodel_name='rppm.muatan.materi.rel',
    #     inverse_name='base_id',
    # )
    
    
    base_muatan_materi_ids = fields.Many2many(
        string=u'Muatan Materi',
        comodel_name='muatan.materi',
        relation='rppm_base_muatan_materi_rel',
        column1='base_id',
        column2='muatan_materi_id',
    )
    
    
    