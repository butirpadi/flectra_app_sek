# -*- coding: utf-8 -*-
from flectra import http

# class SiswaMulti(http.Controller):
#     @http.route('/siswa_multi/siswa_multi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siswa_multi/siswa_multi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siswa_multi.listing', {
#             'root': '/siswa_multi/siswa_multi',
#             'objects': http.request.env['siswa_multi.siswa_multi'].search([]),
#         })

#     @http.route('/siswa_multi/siswa_multi/objects/<model("siswa_multi.siswa_multi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siswa_multi.object', {
#             'object': obj
#         }) 