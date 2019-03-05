# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Query(models.Model):
    _name = 'jjodoo.query'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    roster_emp = fields.One2many('jjodoo.employees', 'employees_ids')
    
    
class Courses(models.Model):
    _name = 'jjodoo.courses'

    course_name = fields.Char(string="Course Name", required=True)
    start_date = fields.Date(requiered=True)
    end_date = fields.Date(requiered=True)
    duration = fields.Integer()
    instructor = fields.Char(string="Instructor´s Name", required=True)
    company = fields.Char(string="Company", required=True)
    code = fields.Char(string="Code", required=True)
    
    
class Employees(models.Model):
    _name = 'jjodoo.employees'
    
    roster = fields.Char(string="Roster", required=True)
    employees_ids = fields.Many2one('jjodoo.query', ondelete='cascade', required=True)
    name = fields.Char(string="Name", required=True)
    date_admission = fields.Date()
    position = fields.Char(string="Position", required=True)
    area = fields.Char(string="Area", required=True)