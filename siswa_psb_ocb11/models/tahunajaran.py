# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from pprint import pprint


class tahunajaran(models.Model):
	_inherit = 'siswa_ocb11.tahunajaran'
	
	@api.model
	def create(self, vals):
		result = super(tahunajaran, self).create(vals)
		
		# auto generate biaya registrasi
		jenjangs = self.env['siswa_ocb11.jenjang'].search([('name', 'ilike', '%')])
		
		print('----------------------------------------')
		print('Generating Biaya Registrasi: ')
		print('----------------------------------------')
		
		for jj in jenjangs:
			biaya_registrasi_ids = self.env['siswa_psb_ocb11.biaya_registrasi'].search([('tahunajaran_id', '=', result.id),
																							('jenjang_id', '=', jj.id)
																						])
			if not biaya_registrasi_ids:
				new_biaya_registrasi = self.env['siswa_psb_ocb11.biaya_registrasi'].create({
					'name' : str(result.name) + ' ' + jj.name,
					'tahunajaran_id' : result.id,
					'jenjang_id' : jj.id
				})
				
				new_biaya_registrasi.recompute_biaya_ta_jenjang()
		
		# generate psb_dashboard
		psb_dash = self.env['psb_dashboard'].create({
				'tahunajaran_id' : result.id
			})
		psb_dash.regenerate_dashboard()
				
		return result
	
	def regenerate_psb_dashboard(self):
		get_dashboard = self.env['psb_dashboard'].search([('tahunajaran_id','=',self.id)])
		if not get_dashboard:
			new_dash = self.env['psb_dashboard'].create({
					'tahunajaran_id' : self.id
				})
			new_dash.regenerate_dashboard()
