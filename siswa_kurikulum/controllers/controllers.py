# -*- coding: utf-8 -*-
from odoo import http

# class SiswaKurikulum(http.Controller):
#     @http.route('/siswa_kurikulum/siswa_kurikulum/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siswa_kurikulum/siswa_kurikulum/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siswa_kurikulum.listing', {
#             'root': '/siswa_kurikulum/siswa_kurikulum',
#             'objects': http.request.env['siswa_kurikulum.siswa_kurikulum'].search([]),
#         })

#     @http.route('/siswa_kurikulum/siswa_kurikulum/objects/<model("siswa_kurikulum.siswa_kurikulum"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siswa_kurikulum.object', {
#             'object': obj
#         })