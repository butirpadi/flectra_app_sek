# -*- coding: utf-8 -*-
from odoo import http

# class SiswaLetter(http.Controller):
#     @http.route('/siswa_letter/siswa_letter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siswa_letter/siswa_letter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siswa_letter.listing', {
#             'root': '/siswa_letter/siswa_letter',
#             'objects': http.request.env['siswa_letter.siswa_letter'].search([]),
#         })

#     @http.route('/siswa_letter/siswa_letter/objects/<model("siswa_letter.siswa_letter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siswa_letter.object', {
#             'object': obj
#         })