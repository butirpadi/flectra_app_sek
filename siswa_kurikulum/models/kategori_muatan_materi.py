# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KategoriMuatanMateri(models.Model):
    _name = 'kategori.muatan.materi'

    code = fields.Char('Kode', required=True)
    name = fields.Text('Nama', required=True)

    # @api.multi
    # def name_get(self):
    #     result = None
    #     for rec in self:
    #         # result.append((inv.id, "%s %s" % (inv.number or TYPES[inv.type], inv.name or '')))
    #         # result.append(rec.name + ' (' + rec.code + ')')
    #         result = rec.name + ' (' + rec.code + ')'

    #     return result

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            # name = '[' + str(record.id) + ']' + ' ' + record.name
            # name = "[%i] %s" % (record.id, record.name)
            name = "{} [{}]".format(record.name, record.code)
            result.append((record.id, name))
        return result
