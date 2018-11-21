# -*- coding: utf-8 -*-

from flectra import models, fields, api, exceptions 
from pprint import pprint


class PsbDashboard(models.Model):
    _name = 'psb_dashboard'
    _order = 'tahunajaran_id desc' 

    tahunajaran_id = fields.Many2one('siswa_ocb11.tahunajaran', string='Tahun Ajaran', ondelete="cascade")
    jumlah_registered = fields.Integer('Registered', default=0)
    jumlah_draft = fields.Integer('Draft', default=0)
    total = fields.Integer('Total', default=0)
    qty_laki = fields.Integer('Laki-laki', default=0)
    qty_perempuan = fields.Integer('Perempuan', default=0)
    color = fields.Integer(string='Color Index') 
    
    def regenerate_dashboard(self):
        calon_sis_ids = self.env['siswa_psb_ocb11.calon_siswa'].search([('tahunajaran_id','=',self.tahunajaran_id.id)])
        
        registered_len = len(self.env['siswa_psb_ocb11.calon_siswa'].search([
                        ('tahunajaran_id','=',self.tahunajaran_id.id),
                        ('state','=','reg')
                    ])
            )
        draft_len = len(self.env['siswa_psb_ocb11.calon_siswa'].search([
                        ('tahunajaran_id','=',self.tahunajaran_id.id),
                        ('state','=','draft')
                    ])
            )    
        laki_len = len(self.env['siswa_psb_ocb11.calon_siswa'].search([
                        ('tahunajaran_id','=',self.tahunajaran_id.id),
                        ('jenis_kelamin','=','laki')
                    ])
            )        
        perempuan_len = len(self.env['siswa_psb_ocb11.calon_siswa'].search([
                        ('tahunajaran_id','=',self.tahunajaran_id.id),
                        ('jenis_kelamin','=','perempuan')
                    ])
            )      
                
        self.write({
                'jumlah_registered' : registered_len,
                'jumlah_draft' : draft_len,
                'total' : len(calon_sis_ids),
                'qty_laki' : laki_len,
                'qty_perempuan' : perempuan_len,
            })
    
    @api.model
    def create(self, vals):
        # fill jenjang_ids
        res = super(PsbDashboard, self).create(vals)
        
        res.regenerate_dashboard()
        
        return res 

    def get_view_laki(self):
        return self.get_view_by_gender('laki')
    
    def get_view_perempuan(self):
        return self.get_view_by_gender('perempuan')
    
    def get_view_by_gender(self, gender):
        return {
                'name': 'Registrasi TA : ' + self.tahunajaran_id.name,
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'siswa_psb_ocb11.calon_siswa',
                'target': 'current',
                'domain' : [('tahunajaran_id', '=', self.tahunajaran_id.id), ('jenis_kelamin', '=', gender)],
                'type': 'ir.actions.act_window',
            }
    
    def get_draft(self):
        return self.get_view_by_state('draft')

    def get_reg(self):
        return self.get_view_by_state('reg')        
    
    def get_view_by_state(self, state):
        return {
                'name': 'Registrasi TA : ' + self.tahunajaran_id.name,
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'siswa_psb_ocb11.calon_siswa',
                'target': 'current',
                'domain' : [('tahunajaran_id', '=', self.tahunajaran_id.id), ('state', '=', state)],
                'type': 'ir.actions.act_window',
            }
    
    def get_view_all(self):
        return {
                'name': 'Registrasi TA : ' + self.tahunajaran_id.name,
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'siswa_psb_ocb11.calon_siswa',
                'target': 'current',
                'domain' : [('tahunajaran_id', '=', self.tahunajaran_id.id)],
                'type': 'ir.actions.act_window',
            }
    
    def create_register(self):
        return {
                'name': 'Registrasi TA : ' + self.tahunajaran_id.name,
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'siswa_psb_ocb11.calon_siswa',
                'target': 'current',
                'context': {'default_tahunajaran_id':self.tahunajaran_id.id},
                'type': 'ir.actions.act_window',
            }
    
    
#     
#     def get_view_rombel_laki(self):
#         return self.get_view_rombel_by_jk('laki')
#     
#     def get_view_rombel_perempuan(self):
#         return self.get_view_rombel_by_jk('perempuan')
#     
#     def get_view_rombel_by_jk(self, jKel):
#         return {
#                 'name': 'Data Siswa ' + self.rombel_id.name + ' ' + self.tahunajaran_id.name,
#                 'view_type': 'form',
#                 'view_mode': 'tree',
#                 'res_model': 'siswa_ocb11.rombel_siswa',
#                 'target': 'current',
#                 'domain' : ['&','&',('tahunajaran_id', '=', self.tahunajaran_id.id), 
#                             ('rombel_id', '=', self.rombel_id.id),
#                             ('jenis_kelamin', '=', jKel)
#                             ],
#                 'type': 'ir.actions.act_window',
#             }
# 
#     @api.depends('rombel_id')
#     def _compute_jumlah_siswa(self):
#         self.lets_compute_jumlah_siswa()
#     
#     def lets_compute_jumlah_siswa(self):
#         print('inside lets compute jumlah siswa')
#         for rec in self:
#             # get jumlah siswa
#             data_siswa = rec.siswa_ids.filtered(lambda r: r.tahunajaran_id.id == rec.tahunajaran_id.id)
#             data_siswa = data_siswa.filtered(lambda r: r.rombel_id.id == rec.rombel_id.id)
#             rec.jumlah_siswa = len(data_siswa)
#             print('Jumlah Siswa : ' + str(len(data_siswa)))
# 
#             #get jumlah siswa laki-laki
#             data_siswa_laki = data_siswa.filtered(lambda r: r.siswa_id.jenis_kelamin == 'laki')
#             rec.jumlah_laki = len(data_siswa_laki)
#             print('Jumlah Siswa Laki2 : ' + str(len(data_siswa_laki)))
# 
#             #get jumlah siswa perempuan
#             data_siswa_perempuan = data_siswa.filtered(lambda r: r.siswa_id.jenis_kelamin == 'perempuan')
#             rec.jumlah_perempuan = len(data_siswa_perempuan)
#             print('Jumlah Siswa Perempuan : ' + str(len(data_siswa_perempuan))) 
