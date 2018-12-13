# -*- coding: utf-8 -*-
from odoo import http

# class InventarisApp(http.Controller):
#     @http.route('/inventaris_app/inventaris_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventaris_app/inventaris_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventaris_app.listing', {
#             'root': '/inventaris_app/inventaris_app',
#             'objects': http.request.env['inventaris_app.inventaris_app'].search([]),
#         })

#     @http.route('/inventaris_app/inventaris_app/objects/<model("inventaris_app.inventaris_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventaris_app.object', {
#             'object': obj
#         })  