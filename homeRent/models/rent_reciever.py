# -*- coding: utf-8 -*-

from odoo import models , fields

class rentReciever(models.Model):
    _name = "rent.reciever"
    _description = "Searching home for living"
    
    name = fields.Char(required = True,default="Name")
    description = fields.Text()
    renting_price = fields.Float()
    sharing = fields.Integer()
    location = fields.Text()
    bachelors = fields.Boolean(default = True)
    deposit_money = fields.Float()
    from_date = fields.Date(default=lambda self:fields.Datetime.now())
    to_date = fields.Date(default=lambda self:fields.Datetime.now())
    contact_no = fields.Integer()
    furnished = fields.Selection(
        string="Furnished",
        selection = [('well-furnished','well-Furnished'),('semi-furnished','Semi-Furnished'),('not-furnished','Not-Furnished')]
    )
    room_type = fields.Selection(
        string="Room Type",
        selection = [('1-rk','1-RK'),('1-bhk','1-BHK'),('2-bhk','2-BHK'),('3-bhk','3-BHK')]
    )
    state = fields.Selection(
        string = "Type",
        selection = [('new','New'),('confirm','Confirm'),('done','Done')],
    )
    tags_ids = fields.Many2many("rent.tags",string="tags")
    offer_ids = fields.One2many("rent.offer","rent_id",string = "Offer id" )