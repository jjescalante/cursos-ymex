# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Query(models.Model):
    _name = 'jjodoo.query'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    session_ids2 = fields.One2many('jjodoo.courses', 'course_id')
    
    
    
class Courses(models.Model):
    _name = 'jjodoo.courses'

    course_name = fields.Char(string="Course Name", required=True)
    start_date = fields.Date(requiered=True)
    end_date = fields.Date(requiered=True)
    duration = fields.Integer(help="Duration in days")
    responsible_id = fields.Many2one(
        'res.users', string="Responsible",
        index=True, ondelete='set null')
    instructor_id = fields.Many2one('res.partner', string="Instructor´s Name", 
                                    domain=['|',('active', '=', False),
                                    ('category_id.name', 'ilike', 'Teacher')])
    company = fields.Char(string="Company", required=True)
    atendees_ids = fields.Many2many('jjodoo.employees', 'name')
    course_id = fields.Many2one('jjodoo.query', ondelete="cascade", 
                                string="Course", required=True)

    
class Employees(models.Model):
    _name = 'jjodoo.employees'
    
    roster = fields.Char(string="Roster", required=True)
    name = fields.Char(string="Name", required=True)
    date_admission = fields.Date()
    position = fields.Char(string="Position", required=True)
    area = fields.Char(string="Area", required=True)
    #session_ids = fields.One2many('jjodoo.courses', 'atendees_ids')