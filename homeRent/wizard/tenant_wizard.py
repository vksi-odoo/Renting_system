# -*- coding: utf-8 -*-
from odoo import fields,models,Command

class tenantWizard(models.TransientModel):
    _name="tenant.wizard"
    _description="This is tenant module"
    
    price = fields.Integer()
    buyer_id = fields.Many2one("res.users")
    salesman_id = fields.Many2one("res.partner")
    
    def action_tenant(self):
        record = self.env["rent.reciever"].browse(self.env.context.get('active_ids'))
        for rec in record:
            rec.write({
                'offer_ids' : [Command.create({
                    'price' : self.price,
                    'partner_id' : self.salesman_id.id
                    
                })]
            })