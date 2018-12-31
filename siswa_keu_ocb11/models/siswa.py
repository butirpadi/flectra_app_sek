# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from pprint import pprint

class siswa(models.Model):
    _inherit = 'res.partner'

    biayas = fields.One2many('siswa_keu_ocb11.siswa_biaya', inverse_name='siswa_id', string='Biaya-biaya') 
    total_biaya = fields.Float('Total Biaya')
    amount_due_biaya = fields.Float('Amount Due')

    def _compute_total_biaya(self):
        print('inside _compute_total_biaya')
        total = 0
        amount = 0
        for by in self.biayas:
            total+=by.harga
            amount+=by.amount_due

        # self.total_biaya = total
        # self.amount_due_biaya = amount
        
        query = "update res_partner \
                set total_biaya = (select sum(harga) from siswa_keu_ocb11_siswa_biaya where siswa_id = " + str(self.id) + "),  \
                amount_due_biaya = (select sum(amount_due) from siswa_keu_ocb11_siswa_biaya where siswa_id = " + str(self.id) + ") \
                where id = " + str(self.id)
        print('running query ... ')
        print(query)
        self.env.cr.execute(query)
    
    @api.multi
    def toggle_active(self):
        self.ensure_one()
        res = super(siswa, self).toggle_active()

        if self.active:
            print('Aktifkan kembali siswa biaya')    
            self.env['siswa_keu_ocb11.siswa_biaya'].search([
                    ('siswa_id','=',self.id),
                    ('active','=',False),
                ]).write({
                    'active' : True
                })
            
            # recalculate keuangan dashboard
            dash_keuangan_id = self.env['ir.model.data'].search([('name','=','default_dashboard_pembayaran')]).res_id
            dash_keuangan = self.env['siswa_keu_ocb11.keuangan_dashboard'].search([('id','=',dash_keuangan_id)])
            for dash in dash_keuangan:
                dash.compute_keuangan()
            
        return res


