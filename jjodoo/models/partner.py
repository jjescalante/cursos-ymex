# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'
    
    supplier = fields.Boolean(default=False, string= "No Instructor")
    session_ids = fields.Many2many(
    				'jjodoo.courses', string="Attended Sessions",
    				readonly=True)