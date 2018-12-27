from odoo import models, fields, api, _


class InventarisSetting(models.Model):
    _name = 'inventaris.setting'

    default_asset_code = fields.Selection([('code', 'System Code'), ('internal_reference', 'Internal Reference')], string="Default Asset Code", default="code")
    
    def execute(self):
        self.write({
                'default_asset_code' : self.default_asset_code
            })  