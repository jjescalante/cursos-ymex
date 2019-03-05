# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Query(models.Model):
    _name = 'jjodoo.query'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    
    
    
class Courses(models.Model):
    _name = 'jjodoo.courses'

    course_name = fields.Char(string="Course Name", required=True)
    start_date = fields.Date(requiered=True)
    end_date = fields.Date(requiered=True)
    duration = fields.Integer(help="Duration in days")
    responsible_id = fields.Many2one(
        'res.users', string="Responsible",
        index=True, ondelete='set null')
    instructor_id = fields.Many2one('res.partner', string="Instructor´s Name")
    company = fields.Char(string="Company", required=True)
    code = fields.Char(string="Code", required=True)
    atendees_ids = fields.Many2many('jjodoo.employees', 'name')
    
    
class Employees(models.Model):
    _name = 'jjodoo.employees'
    
    roster = fields.Char(string="Roster", required=True)
    name = fields.Char(string="Name", required=True)
    date_admission = fields.Date()
    position = fields.Char(string="Position", required=True)
    area = fields.Char(string="Area", required=True)