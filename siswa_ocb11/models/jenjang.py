# -*- coding: utf-8 -*-

from flectra import models, fields, api
from pprint import pprint


class jenjang(models.Model):
    _name = 'siswa_ocb11.jenjang'

    name = fields.Char(string="Nama", required=True)
    sort_order = fields.Integer('Order')
    desc = fields.Char(string="Keterangan")
    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.user.company_id.id)

    @api.model
    def create(self, vals):

        the_company_id = self.env.user.company_id.id
        if 'company_id' in vals:
            the_company_id = vals['company_id']
            
        max_order = self.env['siswa_ocb11.jenjang'].search(
            [('company_id', '=', the_company_id)], order='sort_order desc', limit=1)
        # max_order = self.env['siswa_ocb11.jenjang'].search(
        #     [], order='sort_order desc', limit=1)

        if max_order:
            vals['sort_order'] = max_order.sort_order + 1
        else:
            vals['sort_order'] = 1

        result = super(jenjang, self).create(vals)

        print('--------------------------------------------------------------------------')
        print('Auto generating tahunajaran jenjang for jenjang : ' + result.name)
        print('--------------------------------------------------------------------------')
        # auto generate tahunajaran jenjang
        tahunajaran_ids = self.env['siswa_ocb11.tahunajaran'].search(
            [('id', 'ilike', '%'),
             ('active', 'ilike', '%'),
             ('company_id', '=', result.company_id.id),
             ])

        for ta in tahunajaran_ids:
            # get biaya_registrasi with jenjang
            tahunajaran_jenjang_ids = self.env['siswa_ocb11.tahunajaran_jenjang'].search([('tahunajaran_id', '=', ta.id),
                                                                                          ('jenjang_id', '=', result.id),
                                                                                          ('company_id', '=', ta.company_id
                                                                                           .id),
                                                                                          ])

            if not tahunajaran_jenjang_ids:
                self.env['siswa_ocb11.tahunajaran_jenjang'].create({
                    'name': ta.name + ' ' + result.name,
                    'tahunajaran_id': ta.id,
                    'jenjang_id': result.id,
                    'company_id': ta.company_id.id
                })

        return result

    def shift_up(self):
        if self.sort_order > 1:
            # get prev item

            is_super_user = self.env.user.has_group('base.group_system')

            if is_super_user:
                ta_prev = self.env['siswa_ocb11.jenjang'].search([
                    ('sort_order', '=', self.sort_order - 1),
                    ('company_id', '=', self.company_id.id),
                ])
            else:
                ta_prev = self.env['siswa_ocb11.jenjang'].search([
                    ('sort_order', '=', self.sort_order - 1),
                    ('company_id', '=', self.env.user.company_id.id),
                ])

            # update prev sort_order
            ta_prev.write({
                'sort_order': self.sort_order
            })

            # update mine sort_order
            self.write({
                'sort_order': self.sort_order - 1
            })

    def shift_down(self):
        is_super_user = self.env.user.has_group('base.group_system')

        if is_super_user:
            max_order = self.env['siswa_ocb11.jenjang'].search(
                [('company_id', '=', self.company_id.id)],
                order='sort_order desc', limit=1)
        else:
            max_order = self.env['siswa_ocb11.jenjang'].search(
                [('company_id', '=', self.env.user.company_id.id)],
                order='sort_order desc', limit=1)

        # self.env.cr.execute('select max(sort_order) from siswa_ocb11_jenjang')
        # max_sort_order = self.env.cr.fetchone()
        if self.sort_order < max_order.sort_order:
            if is_super_user:
                ta_next = self.env['siswa_ocb11.jenjang'].search([
                    ('sort_order', '=', self.sort_order + 1),
                    ('company_id', '=', self.company_id.id),
                ])
            else:
                ta_next = self.env['siswa_ocb11.jenjang'].search([
                    ('sort_order', '=', self.sort_order + 1),
                    ('company_id', '=', self.env.user.company_id.id),
                ])

            # # get next item
            # ta_next = self.env['siswa_ocb11.jenjang'].search([
            #     ('sort_order', '=', self.sort_order + 1)
            # ])

            # update prev sort_order
            ta_next.write({
                'sort_order': self.sort_order
            })

            # update mine sort_order
            self.write({
                'sort_order': self.sort_order + 1
            })

    @api.multi
    def unlink(self):
        for rec in self:
            # re order other data yang sort_order nya lebih besar dari ini
            my_sort_order = rec.sort_order
            jenjang_ids = self.env['siswa_ocb11.jenjang'].search(
                [('sort_order', '>', my_sort_order)])

            for jj in jenjang_ids:
                jj.sort_order = jj.sort_order - 1

        return super(jenjang, self).unlink()
