# -*- coding: utf-8 -*-

from odoo import models , fields

class rentTags(models.Model):
    _name= "rent.tags"
    _description = "Rent tags"
    
    name = fields.Char(required=True)