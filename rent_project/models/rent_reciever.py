# -*- coding: utf-8 -*-

from odoo import models

class rentProjectReciever(models.Model):
    _inherit = "rent.reciever"
    
    def action_buy(self):
        self.env['project.task'].create({
            'name' : self.name,
            'partner_id' : self.buyers_id.id,
            'project_id' : 5
        })
        return super(rentProjectReciever,self).action_buy()