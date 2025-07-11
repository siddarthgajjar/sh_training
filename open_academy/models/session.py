# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import timedelta


class Session(models.Model):

    _name = 'academy.session'
    _description = 'Session Info'

    course_id = fields.Many2one(comodel_name='academy.course',
                                string='Course',
                                ondelete='cascade',
                                required=True)

    name = fields.Char(string='Title', 
                       related='course_id.name')

    instructor_id = fields.Many2one(comodel_name='res.partner', 
                                    string='Instructor')

    student_ids = fields.Many2many(comodel_name='res.partner', 
                                   string='Students')
    
    start_date = fields.Date(string='Start Date',
                             default=fields.Date.today)
    
    duration = fields.Integer(string='Session Days',
                             default=1)
    
    end_date = fields.Date(string='End Date', 
                           compute='_compute_end_date',
                           inverse='_inverse_end_date',
                           store=True)
    
    total_price = fields.Float(string='Total Price',
                              related='course_id.total_price')
    
    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
            else:
                duration = timedelta(days=record.duration)
                record.end_date = record.start_date + duration
                
    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date:
                # Friday (5) - Monday (1) = 4
                # As we consider duration from Monday until Friday to be 5 days, + 1
                record.duration = (record.end_date - record.start_date).days + 1
            else:
                continue
                
    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration < 1:
                raise ValidationError('Duration cannot be less 1. An attempt was made to set Duration to %s.' % record.additional_fee)