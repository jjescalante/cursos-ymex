# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Query(models.Model):
    _name = 'jjodoo.query'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

# class jjodoo(models.Model):
#     _name = 'jjodoo.jjodoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
