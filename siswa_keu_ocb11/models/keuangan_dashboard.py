# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.addons import decimal_precision as dp
from datetime import datetime
from pprint import pprint


class keuangan_dashboard(models.Model):
    _name = 'siswa_keu_ocb11.keuangan_dashboard'

    color = fields.Integer(string='Color Index')
    name = fields.Char('Name')
    subtitle = fields.Char('Subtitle')
    rombel_id = fields.Many2one(
        'siswa_ocb11.rombel', string='Rombongan Belajar')
    tahunajaran_id = fields.Many2one(
        'siswa_ocb11.tahunajaran', string='Tahun Ajaran')
    total = fields.Float('Total', default=0.00)
    amount_due = fields.Float('Amount Due', default=0.00)
    paid_amount = fields.Float('Dibayar', default=0.00)
    amount_due_per_tahunajaran = fields.One2many(
        'siswa_keu_ocb11.keuangan_dashboard_tahunajaran_rel', inverse_name='dashboard_id')
    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.user.company_id.id)

    def get_amount_per_ta(self, ta_id):
        am_ta = self.amount_due_per_tahunajaran.search([(
            'tahunajaran_id', '=', ta_id
        )])
        return am_ta.amount_due

    def compute_keuangan(self):
        # get amount due
        self.env.cr.execute(
            "select sum(coalesce(amount_due,0)) from siswa_keu_ocb11_siswa_biaya where state = 'open' and active=True and company_id = " + self.company_id.id)
        total_kas = self.env.cr.fetchone()[0]

        self.amount_due = total_kas

    def compute_kas(self):
        self.env.cr.execute(
            "select sum(coalesce(debet,0))-sum(coalesce(kredit,0)) as saldo from siswa_keu_ocb11_kas where state ='post' and company_id = " + self.company_id.id)
        total_kas = self.env.cr.fetchone()[0]
        self.total = total_kas
        self.amount_due = total_kas
        print('saldo kas (total) : ' + str(self.total))
        print('saldo kas (amount_due) : ' + str(self.amount_due))

    def get_default_name(self):
        default_name = self.env['ir.model.data'].search([
            ('model', '=', 'siswa_keu_ocb11.keuangan_dashboard'),
            ('res_id', '=', self.id),
        ]).name
        return default_name

    @api.model
    def generate_dashboard_for_multi_company(self):
        company_ids = self.env['res.company'].search([('id', '!=', 1)])
        for comp in company_ids:
            # cek apakah data sudah ada atau belum
            dash = self.env['siswa_keu_ocb11.keuangan_dashboard'].search(
                [('company_id', '=', comp.id)])
            if not dash:
                # generate dashboard
                self.env['siswa_keu_ocb11.keuangan_dashboard'].create({
                    'name': 'Tagihan Siswa',
                    'subtitle': 'Jumlah Jatuh Tempo',
                    'company_id': comp.id,
                })
                self.env['siswa_keu_ocb11.keuangan_dashboard'].create({
                    'name': 'Kas',
                    'subtitle': 'Saldo Kas',
                    'company_id': comp.id,
                })
            # generate sequence
            # cek apakah ada atau belum
            seq = self.env['ir.sequence'].search(
                [('code', '=', 'pembayaran.siswa.ocb11')])
            if not seq:
                self.env['ir.sequence'].create({
                    'name': 'Pembayaran Siswa',
                    'code': 'pembayaran.siswa.ocb11',
                    'prefix': 'PAY/%(range_year)s/%(range_month)s/',
                    'padding': 6,
                    'company_id': comp.id,
                })
                self.env['ir.sequence'].create({
                    'name': 'Kas',
                    'code': 'siswa.keu.ocb11.kas',
                    'prefix': 'CASH/%(range_year)s/%(range_month)s/',
                    'padding': 6,
                    'company_id': comp.id,
                })
