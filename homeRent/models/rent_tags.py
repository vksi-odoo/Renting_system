# -*- coding: utf-8 -*-

from odoo import models , fields

class rentTags(models.Model):
    _name= "rent.tags"
    _description = "Rent tags"
    _order = "name"
    
    name = fields.Char(required=True)
    colors= fields.Integer("color index")