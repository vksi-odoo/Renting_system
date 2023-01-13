# -*- coding: utf-8 -*-

from odoo import models,fields,api

class rentType(models.Model):
    _name="rent.type"
    _description="This is the rent type module"
    _order = "name"
    
    name = fields.Char()
    pincode = fields.Integer()
    sequence = fields.Integer("Sequence")
    rentName_ids = fields.One2many('rent.lender','rent_type_id')
    offer_count = fields.Integer('Property Type Count' ,compute="_compute_offer_")
    offer_ids = fields.One2many('rent.offer',"rent_type_id", string="offer")
    
    @api.depends('offer_ids')
    def _compute_offer_(self):
        for record in self:
            record.offer_count = len(record.offer_ids)