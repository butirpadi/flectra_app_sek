# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class biaya(models.Model):
    _name = 'siswa_keu_ocb11.biaya'
    name = fields.Char(string='Nama', requred=True)
    is_bulanan = fields.Boolean('Bulanan',default=False)
    is_different_by_gender = fields.Boolean('Different by Gender?', default=False)
#     is_siswa_baru_only = fields.Boolean('Hanya untuk siswa baru ?', default=False)
#     is_siswa_lama_only = fields.Boolean('Hanya untuk siswa lama ?', default=False)
    is_optional = fields.Boolean('Biaya Opsional?', default=False)
    assign_to = fields.Selection([('baru','Siswa Baru'),('lama', 'Siswa Lama'),('all','All')], string="Assign to", default="all", required=True) 
    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.user.company_id.id)


    @api.model
    def create(self, vals):
        res = super(biaya, self).create(vals)

        # auto generate kas_kategori
        self.env['siswa_keu_ocb11.kas_kategori'].create({
            'name' : res.name,
            'tipe' : 'in',
            'is_biaya_account' : True,
            'biaya_id' : res.id,
            'company_id' : res.company_id.id
        })

        return res
    
    def regenerate_akun_kas(self):
        # cek apakah sudah ada atau belum
        akun_kas = self.env['siswa_keu_ocb11.kas_kategori'].search([('biaya_id','=',self.id)])
        if akun_kas:
            print('ada')
        else:
            # generate akun kas
            self.env['siswa_keu_ocb11.kas_kategori'].create({
                'name' : self.name,
                'tipe' : 'in',
                'is_biaya_account' : True,
                'biaya_id' : self.id,
                'company_id' : self.company_id.id
            })
