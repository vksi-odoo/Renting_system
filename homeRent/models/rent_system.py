# -*- coding: utf-8 -*-

from odoo import models, fields

class rentSystem(models.Model):
    _name = "rent.system"
    _description = "Home renting system"
    _inherit = ['mail.thread','mail.activity.mixin']
    
    name= fields.Char(required = True,default = "Name")
    description = fields.Text()
    contact_no = fields.Integer()
    address = fields.Text()
    state = fields.Selection(
        string="state",
        selection = [('new','New'),('confirm','Confirm'),('done','Done')]
    )
    
    