# -*- coding: utf-8 -*-

from odoo import models , fields
from odoo.exceptions import ValidationError

class rentOffer(models.Model):
    _name="rent.offer"
    _description = "Home rent offer"
    _order= "price desc"
    
    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection = [('accepted','Accepted'),('refused','Refused')]
    )
    partner_id = fields.Many2one("res.partner",string="Partner id")
    rents_id = fields.Many2one("rent.reciever",string ="Renting id")
    rent_id = fields.Many2one("rent.lender",string = "Rent id")
    pg_id = fields.Many2one("pg.pg",string="PG id")
    
    rent_type_id = fields.Many2one("rent.type",related="rent_id.rent_type_id",store=True,string = "Rent Types")

    def action_accept_lender(self):
        for record in self.search([('status','=','accepted')]):
            if record.rent_id == self.rent_id:
                raise ValidationError('Cant accept more than one')
            else:
                for i in record:
                    record.status='refused'
        self.status = 'accepted'
        self.rent_id.state='confirm'
        self.rent_id.renting_price = self.price
        self.rent_id.buyers_id = self.partner_id
    
    def action_refused_lender(self):
        for record in self:
            record.status= 'refused'
    
    def action_accept_receiver(self):
        for record in self.search([('status','=','accepted')]):
            if record.rents_id == self.rents_id:
                raise ValidationError('Cant acept more than one')
            else:
                for i in record:
                    record.status='refused'
        self.status='accepted'
        self.rents_id.state='confirm'
        self.rents_id.renting_price = self.price
        self.rents_id.buyers_id = self.partner_id
    
    def action_refused_receiver(self):
        for record in self:
            record.status = 'refused'
    
    def action_accept_pg(self):
        for record in self.search([('status','=','accepted')]):
            if record.pg_id == self.pg_id:
                raise ValidationError('Cant accept more than one')
            else:
                for i in record:
                    record.status='refused'
        self.status='accepted'
        self.pg_id.state='confirm'
        self.pg_id.pg_price=self.price
        self.pg_id.buyers_id = self.partner_id
    
    def action_refused_pg(self):
        for record in self:
            record.status = 'refused'    
    
    