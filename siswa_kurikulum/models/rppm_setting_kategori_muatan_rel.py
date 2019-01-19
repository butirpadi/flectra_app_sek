# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RppmSettingKategoriMuatanRel(models.Model):
    _name = 'rppm.setting.kategori.muatan.rel'

    setting_id = fields.Many2one(
        string=u'Setting',
        comodel_name='rppm.setting',
        ondelete='cascade',
    )

    kategori_muatan_id = fields.Many2one(
        string=u'Kategori Muatan',
        comodel_name='kategori.muatan.materi',
        ondelete='restrict',
    )

    sort_order = fields.Integer('Order', default=lambda self: self.get_order())

    @api.multi
    def get_order(self):
        for rec in self:
            max_order = self.env['rppm.setting.kategori.muatan.rel'].search(
                [], order='sort_order desc', limit=1)
            print('Default sort order')
            print(max_order.sort_order + 1)
            return max_order.sort_order + 1

    @api.multi
    def shiftUp(self):
        for rec in self:
            if self.sort_order > 1:
                ta_prev = self.env['rppm.setting.kategori.muatan.rel'].search([
                    ('sort_order', '=', rec.sort_order - 1)
                ])

                # update prev sort_order
                ta_prev.write({
                    'sort_order': rec.sort_order
                })

                # update mine sort_order
                rec.write({
                    'sort_order': rec.sort_order - 1
                })

    @api.multi
    def shiftDown(self):
        for rec in self:
            # self.env.cr.execute('select max(sort_order) from siswa_ocb11_tahunajaran')
            # max_order = self.env.cr.fetchone()
            max_order = self.env['rppm.setting.kategori.muatan.rel'].search(
                [], order='sort_order desc', limit=1)
            max_order = max_order.sort_order
            if rec.sort_order < max_order:
                # get next item
                ta_next = self.env['rppm.setting.kategori.muatan.rel'].search([
                    ('sort_order', '=', rec.sort_order + 1)
                ])

                # update prev sort_order
                ta_next.write({
                    'sort_order': rec.sort_order
                })

                # update mine sort_order
                rec.write({
                    'sort_order': rec.sort_order + 1
                })


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
