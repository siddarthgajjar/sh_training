# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course Info'

    name = fields.Char(string='Title', required=True)
    
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level', 
                             selection=[('beginner', 'Beginner'), 
                                        ('intermediate', 'Intermediate'),
                                        ('advanced', 'Advanced')], 
                             copy=False)
    
    # toggles global visibility of the record, if set to False the record is invisible in most searches and listing.
    active = fields.Boolean(string='Active', 
                            default=True)
    
    base_price = fields.Float(string='Base Price', 
                              default=0.00)
    
    additional_fee = fields.Float(string='Additional Fee', 
                                  default=10.00)
    
    total_price = fields.Float(string='Total Price', 
                               compute='_compute_total_price', 
                               store=True)
    
    session_ids = fields.One2many(comodel_name='academy.session', 
                                  inverse_name='course_id', 
                                  string='Sessions')

    @api.depends('base_price', 'additional_fee')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.base_price + record.additional_fee

    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise UserError(_('Additional Fees cannot be less than 10.00. An attempt was made to set Additional Fees to %s.') % record.additional_fee)
          
    @api.constrains('base_price')
    def _check_base_price(self):
        for record in self:
            if record.base_price < 0.00:
                raise ValidationError(_('Base Price cannot be set as negative. An attempt was made to set Base Price to %s.') % record.base_price)
