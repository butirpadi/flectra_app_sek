# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from pprint import pprint


class Barang(models.Model):
    _name = 'inventaris.barang'
    
    name = fields.Char('Name')
    nama = fields.Char('Name')
    code = fields.Char('System Code', default="New")
    internal_reference = fields.Char('Kode')
    serial_number = fields.Char('Serial Number')
    panjang = fields.Float('Panjang', default=0.0)
    lebar = fields.Float('Lebar', default=0.0)
    tinggi = fields.Float('Tinggi', default=0.0)
    volume = fields.Float('Volume', default=0.0)
    color_id = fields.Many2one('inventaris.color', ondelete="restrict")
    kategori_id = fields.Many2one('inventaris.kategori', string="Kategori", ondelete="restrict")
    nilai_penyusutan = fields.Float('Nilai Penyusutan', default=0.0)
    interval_penyusutan = fields.Integer('Bulan')
    lokasi_id = fields.Many2one('inventaris.lokasi', string="Lokasi", ondelete="restrict")
    lokasi_move_id = fields.One2many('inventaris.barang.move', inverse_name="barang_id", string="Lokasi Moving", context={'active_test': False})
    brand_id = fields.Many2one('inventaris.brand', string="Brand", ondelete="restrict")
    satuan_id = fields.Many2one('inventaris.satuan', string="Satuan", ondelete="restrict")
    tanggal_pengadaan = fields.Date('Tanggal Pengadaan')
    purchase_date = fields.Date('Purchase Date')
    cost = fields.Float('Harga', default=0.0)
    purchase_number = fields.Char('Purchase Number')
    partner_id = fields.Many2one('res.partner', string="Vendor", domain=[('supplier', '=', True)])
    desc = fields.Text('Keterangan')
    qty = fields.Integer('Quantity', default=1) 
    kondisi = fields.Selection([('normal', 'Normal'), ('rusak', 'Rusak')], string='Kondisi', required=True, default='normal')
    sumber_id = fields.Many2one('inventaris.sumber.dana')
    scrap_date = fields.Datetime('Scrap Date')
    
    def action_scrap(self):
        self.kondisi = 'rusak'
        print('Scrap this asset')
    
    @api.onchange('tanggal_pengadaan')
    def tanggal_pengadaan_onchange(self):
        self.purchase_date = self.tanggal_pengadaan
    
    @api.onchange('nama')
    def nama_onchange(self):
        setting_id = self.env.ref('inventaris.inventaris_default_setting').id
        default_code = self.env['inventaris.setting'].search([('id', '=', setting_id)])
        
        if default_code.default_asset_code == 'internal_reference':
            self.name = str(self.nama) + ' ' + str(self.internal_reference)
        else:
            self.name = str(self.nama) + ' ' + str(self.code)
    
    @api.onchange('internal_reference')
    def internal_reference_onchange(self):
        setting_id = self.env.ref('inventaris.inventaris_default_setting').id
        default_code = self.env['inventaris.setting'].search([('id', '=', setting_id)])
        
        if default_code.default_asset_code == 'internal_reference':
            self.name = str(self.nama) + ' ' + str(self.internal_reference)
        else:
            self.name = str(self.nama) + ' ' + str(self.code)
    
    @api.model
    def create(self, vals):
        print('Create barang')
        if vals.get('code', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['code'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('barang.code.seq') or _('New')
            else:
                vals['code'] = self.env['ir.sequence'].next_by_code('barang.code.seq') or _('New')
        
        # set name with default code
#         default_code = self.env['inventaris.setting']
        setting_id = self.env.ref('inventaris.inventaris_default_setting').id
        default_code = self.env['inventaris.setting'].search([('id', '=', setting_id)])
        
        if default_code.default_asset_code == 'internal_reference':
            vals['name'] = vals['nama'] + ' ' + str(vals['internal_reference'])
#         vals['name'] = 
        
        pprint(vals)
        result = super(Barang, self).create(vals)
         
        # add first movingz
        result.lokasi_move_id = [(0, 0, {
                'barang_id' : result.id,
                'lokasi_id' : result.lokasi_id.id
            })]
        
        # set name if default_code is code
        if default_code.default_asset_code == 'code':
            result.name = result.nama + ' ' + result.code
         
        return result
    
#     @api.multi
#     def write(self, vals):
#         res = super(Barang, self).write(vals)
#         
# #         # update name
# #         setting_id = self.env.ref('inventaris.inventaris_default_setting').id
# #         default_code = self.env['inventaris.setting'].search([('id', '=', setting_id)])
# #          
# #         if default_code.default_asset_code == 'internal_reference':
# #             res.name = res.nama + ' ' + str(res.internal_reference)
# #         else:
# #             res.name = res.nama + ' ' + res.code            
#             
#         return res
        
