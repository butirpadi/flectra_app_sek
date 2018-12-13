# -*- coding: utf-8 -*-
from flectra import http

# class BasicInstallOcb11(http.Controller):
#     @http.route('/basic_install_ocb11/basic_install_ocb11/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/basic_install_ocb11/basic_install_ocb11/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('basic_install_ocb11.listing', {
#             'root': '/basic_install_ocb11/basic_install_ocb11',
#             'objects': http.request.env['basic_install_ocb11.basic_install_ocb11'].search([]),
#         })

#     @http.route('/basic_install_ocb11/basic_install_ocb11/objects/<model("basic_install_ocb11.basic_install_ocb11"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('basic_install_ocb11.object', {
#             'object': obj
#         })  