# -*- coding: utf-8 -*-
from flectra import http

# class DefaultSettingForIndonesianApp(http.Controller):
#     @http.route('/default_setting_for_indonesian_app/default_setting_for_indonesian_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/default_setting_for_indonesian_app/default_setting_for_indonesian_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('default_setting_for_indonesian_app.listing', {
#             'root': '/default_setting_for_indonesian_app/default_setting_for_indonesian_app',
#             'objects': http.request.env['default_setting_for_indonesian_app.default_setting_for_indonesian_app'].search([]),
#         })

#     @http.route('/default_setting_for_indonesian_app/default_setting_for_indonesian_app/objects/<model("default_setting_for_indonesian_app.default_setting_for_indonesian_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('default_setting_for_indonesian_app.object', {
#             'object': obj
#         }) 