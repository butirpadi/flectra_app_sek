# -*- coding: utf-8 -*-
from odoo import http

# class TkSakha(http.Controller):
#     @http.route('/tk_sakha/tk_sakha/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tk_sakha/tk_sakha/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tk_sakha.listing', {
#             'root': '/tk_sakha/tk_sakha',
#             'objects': http.request.env['tk_sakha.tk_sakha'].search([]),
#         })

#     @http.route('/tk_sakha/tk_sakha/objects/<model("tk_sakha.tk_sakha"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tk_sakha.object', {
#             'object': obj
#         }) 