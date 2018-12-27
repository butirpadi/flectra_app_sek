from odoo import models, fields, api
from pprint import pprint
from datetime import datetime


class WizardSuratTagihan(models.Model):
    _name = 'siswa.wizard.surat.tagihan'

    state = fields.Selection([('draft', 'Draft'), ('post', 'Posted')],
                             string='State', required=True, default='draft')
    name = fields.Char('name', default="Surat Tagihan")
    tahunajaran_id = fields.Many2one(
        'siswa_ocb11.tahunajaran', string="Tahun Ajaran")
    # jenjang_ids = fields.Many2many('siswa_ocb11.jenjang', string="Jenjang")
    rombel_ids = fields.Many2many(
        'siswa_ocb11.rombel', string="Rombongan Belajar")
    siswa_ids = fields.Many2many('res.partner', string="Siswa", domain=[
                                 ('is_siswa', '=', True)])
    tagihan_biaya_ids = fields.One2many(
        string=u'Biaya',
        comodel_name='wizard.surat.tagihan.biaya.rel',
        inverse_name='wizard_id',
    )
    surat_siswa_ids = fields.One2many(
        string=u'Surat',
        comodel_name='surat.tagihan.siswa.rel',
        inverse_name='wizard_id'
    )

    @api.multi
    def submit_wizard(self):
        surat_res_id = self.env['ir.model.data'].search(
            [('name', '=', '__siswa_letter_surat_tagihan_')]).res_id
        surat_id = self.env['siswa.surat'].search([('id', '=', surat_res_id)])
        surat_seq = surat_id.surat_tagihan_seq
        surat_prefix = surat_id.surat_tagihan_prefix

        surat_data_temp = []

        for siswa in self.siswa_ids:
            # generate surat nomor
            nomor_surat = surat_prefix + "/" + "/000" + str(surat_seq)
            surat_seq += 1

            # # get biaya
            # total_tagihan = 0.0
            # siswa_biaya_temp = []
            # for tag_by in self.tagihan_biaya_ids:
            #     if tag_by.is_bulanan:
            #         siswa_biaya_id = self.env['siswa_keu_ocb11.siswa_biaya'].search(
            #             ['&', '&', '&', '&', ('state', '=', 'open'), ('siswa_id', '=', siswa.id), ('biaya_id', '=', tag_by.biaya_id.id), ('tahunajaran_id', '=', self.tahunajaran_id.id), ('bulan', '=', tag_by.bulan)])
            #     else:
            #         siswa_biaya_id = self.env['siswa_keu_ocb11.siswa_biaya'].search(
            #             ['&', '&', '&', ('state', '=', 'open'), ('siswa_id', '=', siswa.id), ('biaya_id', '=', tag_by.biaya_id.id), ('tahunajaran_id', '=', self.tahunajaran_id.id)])

            #     siswa_biaya_temp.append((4, siswa_biaya_id.id))
            #     total_tagihan += siswa_biaya_id.amount_due

            surat_data_temp.append([0, 0, {
                'siswa_id': siswa.id,
                'name': nomor_surat,
                # 'tagihan_siswa_biaya_ids': siswa_biaya_temp,
                # 'total_tagihan': total_tagihan
            }])

        self.surat_siswa_ids = surat_data_temp
        self.state = 'post'

        for srt in self.surat_siswa_ids:
            # get biaya
            total_tagihan = 0.0
            # siswa_biaya_temp = []
            for tag_by in self.tagihan_biaya_ids:
                if tag_by.is_bulanan:
                    siswa_biaya_id = self.env['siswa_keu_ocb11.siswa_biaya'].search(
                        ['&', '&', '&', '&', ('state', '=', 'open'), ('siswa_id', '=', srt.siswa_id.id), ('biaya_id', '=', tag_by.biaya_id.id), ('tahunajaran_id', '=', self.tahunajaran_id.id), ('bulan', '=', tag_by.bulan)])
                else:
                    siswa_biaya_id = self.env['siswa_keu_ocb11.siswa_biaya'].search(
                        ['&', '&', '&', ('state', '=', 'open'), ('siswa_id', '=', srt.siswa_id.id), ('biaya_id', '=', tag_by.biaya_id.id), ('tahunajaran_id', '=', self.tahunajaran_id.id)])

                # siswa_biaya_temp.append((4, siswa_biaya_id.id))
                if siswa_biaya_id:
                    total_tagihan += siswa_biaya_id.amount_due
                    self.env.cr.execute('insert into surat_tagihan_siswa_biaya_rel (surat_tagihan_siswa_rel_id, siswa_biaya_id) values (' + str(
                        srt.id) + ',' + str(siswa_biaya_id.id) + ')')

            # Update total tagihan
            srt.total_tagihan = total_tagihan

        # update surat_seq
        surat_id.write({
            'surat_tagihan_seq': surat_seq
        })

        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'siswa.wizard.surat.tagihan',
            'target': 'current',
            'res_id': self.id,
            'type': 'ir.actions.act_window',
            # 'view_id': self.env.ref('siswa_keu_ocb11.wizard_pembayaran_harian_form').id,
        }

    # @api.onchange('jenjang_ids')
    # def jenjang_id_onchange(self):
    #     return self.set_domain_rombel_ids()

    @api.onchange('rombel_ids')
    def rombel_id_onchange(self):
        if self.rombel_ids:
            domain = {'siswa_ids': [
                ('active_rombel_id', 'in', self.rombel_ids.ids), ('is_siswa', '=', True)]}
        else:
            domain = {'siswa_ids': [('is_siswa', '=', True)]}

        return {'domain': domain, 'value': {'siswa_ids': []}}

    # def set_domain_rombel_ids(self):
    #     domain = {'rombel_ids': [('jenjang_id', 'in', self.jenjang_ids.ids)]}
    #     return {'domain': domain, 'value': {'rombel_ids': []}}

    def set_domain_siswa_ids(self):
        # if self.rombel_ids:
        #     domain = {'siswa_ids': [
        #         ('active_rombel_id', 'in', self.rombel_ids.ids)]}
        # else:
        #     domain = {'siswa_ids': []}

        # tampilkan sesuai filter
        domain = {'siswa_ids': [
            ('active_rombel_id', 'in', self.rombel_ids.ids), ('is_siswa', '=', True)]}

        return {'domain': domain, 'value': {'siswa_ids': []}}
