# -*- coding: utf-8 -*-
from odoo import http

# class SiswaEmployee(http.Controller):
#     @http.route('/siswa_employee/siswa_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siswa_employee/siswa_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siswa_employee.listing', {
#             'root': '/siswa_employee/siswa_employee',
#             'objects': http.request.env['siswa_employee.siswa_employee'].search([]),
#         })

#     @http.route('/siswa_employee/siswa_employee/objects/<model("siswa_employee.siswa_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siswa_employee.object', {
#             'object': obj
#         })