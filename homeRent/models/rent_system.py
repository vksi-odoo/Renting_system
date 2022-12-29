# -*- coding: utf-8 -*-

from odoo import models, fields

class rentSystem(models.Model):
    _name = "rent.system"
    _description = "Home renting system"
    
    name = fields.Char(required=True,default="Name")
    description = fields.Text("Description",copy=False,required=True,default="What is your furthur requirment?")
    from_date = fields.Date(default = lambda self: fields.Datetime.now())
    to_date= fields.Date(default=lambda self: fields.Datetime.now())
    renting_price = fields.Float()
    sharing = fields.Integer()
    location = fields.Text()
    bachelors = fields.Boolean(default = True)
    furnished = fields.Selection(
        string="Furnished",
        selection = [('full-furnished','Full-Furnished'),('semi-furnished','Semi-Furnished'),('not-furnished','Not-Furnished')]
    )
    room_type = fields.Selection(
        string="Room Type",
        selection = [('1rk','1RK'),('1bhk','1BHK'),('2bhk','2BHK'),('3bhk','3BHK')]
    )
    purpose = fields.Selection(
        string="Purpose",
        selection = [('lender','Lender'),('reciever','Reciever')]
    )
    state = fields.Selection(
        string="state",
        selection = [('new','New'),('confirm','Confirm'),('done','Done')]
    )

    