# -*- coding: utf-8 -*-

from odoo import models , fields

class rentOffer(models.Model):
    _name="rent.offer"
    _description = "Home rent offer"
    
    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection = [('accepted','Accepted'),('refused','refused')]
    )
    partner_id = fields.Many2one("res.partner",string="Partner id")
    rent_id = fields.Many2one("rent.reciever",string ="rent_id")
    rent_id = fields.Many2one("rent.lender",string = "rent_id")