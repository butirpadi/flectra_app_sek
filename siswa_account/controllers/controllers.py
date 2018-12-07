# -*- coding: utf-8 -*-
from odoo import http

# class SiswaAccount(http.Controller):
#     @http.route('/siswa_account/siswa_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siswa_account/siswa_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siswa_account.listing', {
#             'root': '/siswa_account/siswa_account',
#             'objects': http.request.env['siswa_account.siswa_account'].search([]),
#         })

#     @http.route('/siswa_account/siswa_account/objects/<model("siswa_account.siswa_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siswa_account.object', {
#             'object': obj
#         })