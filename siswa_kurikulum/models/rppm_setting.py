# -*- coding: utf-8 -*-

from odoo import models, fields, api
from pprint import pprint


class RppmSetting(models.Model):
    _name = 'rppm.setting'

    name = fields.Char('Name')
    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Ajaran', required=True,
                                     default=lambda x: x.env['siswa_ocb11.tahunajaran'].search([('active', '=', True)]))
    kategori_muatan_ids = fields.One2many(
        string=u'Kategori Muatan',
        comodel_name='rppm.setting.kategori.muatan.rel',
        inverse_name='setting_id',
    )
    is_two_step_approval = fields.Boolean('Two level approval', default=False)
    first_approval_id = fields.Many2one('hr.employee', string="First Approval")
    first_job_id = fields.Many2one('hr.job', string="Job Position", related="first_approval_id.job_id")
    second_approval_id = fields.Many2one('hr.employee', string="Second Approval")
    second_job_id = fields.Many2one('hr.job', string="Job Position", related="second_approval_id.job_id")

    @api.depends('tahunajaran_id')
    def _onchange_tahunajaran_id(self):
        self.name = self.tahunajaran_id.name

    @api.model
    def create(self, vals):
        # set name
        if 'tahunajaran_id' in vals:
            tahunajaran = self.env['siswa_ocb11.tahunajaran'].search([('id','=',vals['tahunajaran_id'])])
            vals['name'] = tahunajaran.name

        is_update_muatan = False
        if 'kategori_muatan_ids' in vals:
            is_update_muatan = True

        res = super(RppmSetting, self).create(vals)
        if is_update_muatan:
            sort_order = 0
            for muatan in res.kategori_muatan_ids:
                muatan.sort_order = sort_order + 1
                sort_order += 1

        return res

    @api.multi
    def write(self, vals):
        res = None
        is_update_muatan = False
        if 'kategori_muatan_ids' in vals:
            is_update_muatan = True

        for rec in self:
            res = super(RppmSetting, self).write(vals)
            # update sort_order on muatan materi
            if is_update_muatan:
                sort_order = 0
                for muatan in rec.kategori_muatan_ids:
                    muatan.sort_order = sort_order + 1
                    sort_order += 1

        return res
