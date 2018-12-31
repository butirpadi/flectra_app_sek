from odoo import models, fields, api, _
from pprint import pprint
from datetime import datetime

class WizardScrap(models.TransientModel):
    _name = 'inventaris.wizard.scrap'
    
    name = fields.Char('Name', default="0")
    barang_id = fields.Many2one('inventaris.barang', string="Asset", required=True, ondelete="cascade", domain=[('kondisi','=','normal')])
    lokasi_id = fields.Many2one('inventaris.lokasi', string="Lokasi")
    scrap_date = fields.Datetime('Scrap Date', default=datetime.now())
    
    current_lokasi_id = fields.Many2one('inventaris.lokasi', related="barang_id.lokasi_id")
    
    @api.multi
    def action_save(self):
        self.ensure_one()
        
        # set kondisi barang
        self.barang_id.write({
                'kondisi' : 'rusak',
                'scrap_date' : self.scrap_date
            })
        
        # set jika di mutasikan
        if self.lokasi_id:
            self.env['inventaris.barang.move'].search([('barang_id','=',self.barang_id.id)]).write({
                'active' : False
            })
        
            # add data to inventaris_barang_move
            self.env['inventaris.barang.move'].create({
                    'barang_id' : self.barang_id.id,
                    'lokasi_id' : self.lokasi_id.id,
                    'move_date' : self.scrap_date
                })
            
            # set current location on asset/barang
            self.barang_id.write({
                    'lokasi_id' : self.lokasi_id.id
                })
