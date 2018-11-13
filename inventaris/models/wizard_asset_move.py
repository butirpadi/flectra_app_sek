from flectra import models, fields, api, _
from pprint import pprint
from datetime import datetime

class wizard_asset_move(models.TransientModel):
    _name = 'inventaris.wizard.asset.move'
    
    name = fields.Char('Name', default="0")
    barang_id = fields.Many2one('inventaris.barang', string="Asset", required=True, ondelete="cascade")
    lokasi_id = fields.Many2one('inventaris.lokasi', string="Lokasi")
    move_date = fields.Datetime('Move Date', default=datetime.now())
    
    current_lokasi_id = fields.Many2one('inventaris.lokasi', related="barang_id.lokasi_id")
    
    @api.multi
    def action_save(self):
        self.ensure_one()
        # set not active to other data
        # self.env.cr.execute('update inventaris_barang_move set active=false where barang_id = ' + str(self.barang_id.id))
        self.env['inventaris.barang.move'].search([('barang_id','=',self.barang_id.id)]).write({
                'active' : False
            })
        
        # add data to inventaris_barang_move
        self.env['inventaris.barang.move'].create({
                'barang_id' : self.barang_id.id,
                'lokasi_id' : self.lokasi_id.id,
                'move_date' : self.move_date
            })
        
        # set current location on asset/barang
        self.barang_id.write({
                'lokasi_id' : self.lokasi_id.id
            })
