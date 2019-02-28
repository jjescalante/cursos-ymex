# -*- coding: utf-8 -*-
from odoo import http

# class Jjodoo(http.Controller):
#     @http.route('/jjodoo/jjodoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jjodoo/jjodoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jjodoo.listing', {
#             'root': '/jjodoo/jjodoo',
#             'objects': http.request.env['jjodoo.jjodoo'].search([]),
#         })

#     @http.route('/jjodoo/jjodoo/objects/<model("jjodoo.jjodoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jjodoo.object', {
#             'object': obj
#         })