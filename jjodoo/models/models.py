# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import time
from datetime import timedelta


class Query(models.Model):
    _name = 'jjodoo.query'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    session_ids2 = fields.One2many('jjodoo.courses', 'course_id')
    _sql_constraints = [('name_description_check',
                         'CHECK( name != description )',
                         "The title of course should not be the description"),
                        ('name_unique', 'UNIQUE(name)',
                         "The course title must be unique", ),
                        ]
    
    
    
class Courses(models.Model):
    _name = 'jjodoo.courses'

    course_name = fields.Char(string="Course Name", required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(store=True,
                           compute='_get_end_date', inverse='_set_end_date')
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    responsible_id = fields.Many2one(
        'res.users', string="Responsible",
        index=True, ondelete='set null')
    instructor_id = fields.Many2one('res.partner', string="Instructor´s Name", 
                                    domain=['|',('supplier', '=', False),
                                    ('category_id.name', 'ilike', 'Teacher')])
    company = fields.Char(string="Company", required=True)
    attendees_ids = fields.Many2many('jjodoo.employees', 'session_id')
    course_id = fields.Many2one('jjodoo.query', ondelete="cascade", 
                                string="Course", required=True)
    attendees_count = fields.Integer(compute='_get_attendees_count',
                                     store=True)
    color = fields.Float()
    hours = fields.Float(
        string = "Duration in hours",
        compute='_get_hours', inverse='_set_hours')
    evidence = fields.Char(string="evidence")
        
   
    @api.depends('duration')
    def _get_hours(self):
        for r in self:
            r.hours = r.duration * 24
            
    def _set_hours(self):
        for r in self:
            r.duration = r.hours / 24
                                     
    
    @api.depends('attendees_ids')
    def _get_attendees_count(self):
        for record in self:
            record.attendees_count = len(record.attendees_ids)
                                
                                
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for record in self.filtered('start_date'):
            start_date = fields.Datetime.from_string(record.start_date)
            record.end_date = start_date + timedelta(days=record.duration,
                                                     seconds=-1)

    def _set_end_date(self):
        for record in self.filtered('start_date'):
            start_date = fields.Datetime.from_string(record.start_date)
            end_date = fields.Datetime.from_string(record.end_date)
            record.duration = (end_date - start_date).days + 1
    

class Employees(models.Model):
    _name = 'jjodoo.employees'
    
    roster = fields.Char(string="Roster", required=True)
    name = fields.Char(string="Name", required=True)
    date_admission = fields.Date()
    position = fields.Char(string="Position", required=True)
    area = fields.Char(string="Area", required=True)
    #session_id = fields.Many2many('jjodoo.courses', 'course_id', store=True)
    session_id = fields.Char(compute="_get_session", store=True)
    
    tagsids = []
    
    def _get_session(self):
        for record in self:
            tagids = record.attendees_ids
            record.write({'courses_id': [(6,0,tagids)]})
            manuf_tagids = []