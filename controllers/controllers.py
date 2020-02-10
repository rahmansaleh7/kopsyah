# -*- coding: utf-8 -*-
from odoo import http

# class Kopsyah(http.Controller):
#     @http.route('/kopsyah/kopsyah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kopsyah/kopsyah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kopsyah.listing', {
#             'root': '/kopsyah/kopsyah',
#             'objects': http.request.env['kopsyah.kopsyah'].search([]),
#         })

#     @http.route('/kopsyah/kopsyah/objects/<model("kopsyah.kopsyah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kopsyah.object', {
#             'object': obj
#         })