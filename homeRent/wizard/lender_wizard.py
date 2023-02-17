# -*- coding: utf-8 -*-
from odoo import models, _ , fields,Command

class lenderWizard(models.TransientModel):
    _name= 'lender.wizard'
    _description = "Rent Lender Wizard"
    
    price = fields.Integer()
    buyer_id = fields.Many2one("res.users", string="Partner Id") 
    salesman_id  = fields.Many2one("res.partner",string="Salesman") 
    def action_done(self):
        record = self.env['rent.lender'].browse(self.env.context.get('active_ids'))
        for rec in record:
            rec.write({
                'offer_ids' : [Command.create({
                    'price' : self.price,
                    'partner_id' : self.salesman_id.id
                })]
            })  
    