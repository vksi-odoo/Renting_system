# -*- coding: utf-8 -*-
from odoo import models,fields,Command

class pgWizard(models.TransientModel):
    _name= "pg.wizard"
    _description="This is wizard model for Paying Guest"
    
    price = fields.Integer()
    buyer_id = fields.Many2one("res.partner" ,string ="Partner_id")
    salesman_id = fields.Many2one("res.users" , string="Salesman")
    
    def action_pg(self):
        record = self.env['pg.pg'].browse(self.env.context.get('active_ids'))
        for rec in record:
            rec.write({
                'offer_ids' : [Command.create({
                    'price' : self.price,
                    'partner_id' : self.buyer_id.id
                })]
            })