# -*- coding: utf-8 -*-

from odoo import models,fields

class inheritedModel(models.Model):
    _inherit = "res.users"
    
    property_ids = fields.One2many('rent.lender','salesperson_id')
    # properties_ids = fields.One2many('rent.reciever','salesperson_id')