# -*- coding: utf-8 -*-

from odoo import models,Command

class rentLender(models.Model):
    _inherit= "rent.reciever"
    
    def action_buy(self):
        self.env['account.move'].create(
            {
                'partner_id' : self.buyers_id.id,
                'move_type' : 'out_invoice',
                'invoice_line_ids' : [
                    Command.create({
                        'name' : self.name,
                        'quantity' : 1,
                        'price_unit' : 100
                    })
                ]
            }
        )
        return super(rentLender,self).action_buy()