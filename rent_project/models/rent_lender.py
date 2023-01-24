# -*- coding: utf-8 -*-

from odoo import models

class rentProjectLender(models.Model):
    _inherit = "rent.lender"
    
    def action_sold(self):
        self.env['project.task'].create({
            'name' : self.name,
            'partner_id' : self.buyers_id.id,
            'project_id' : 4
        })
        return super(rentProjectLender,self).action_sold()