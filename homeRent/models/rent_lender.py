# -*- coding: utf-8 -*-

from odoo import models, fields

class rentLender(models.Model):
    _name = "rent.lender"
    _description = "Giving my room for rent"
    
    name = fields.Char(required=True,default="Name")
    description = fields.Text("Description",copy=False,default="What is your furthur requirment?")
    from_date = fields.Date(default = lambda self: fields.Datetime.now())
    to_date= fields.Date(default=lambda self: fields.Datetime.now())
    renting_price = fields.Float()
    sharing = fields.Integer()
    location = fields.Text()
    bachelors = fields.Boolean(default = True)
    deposit_money = fields.Float()
    contact_no = fields.Integer()
    furnished = fields.Selection(
        string="Furnished",
        selection = [('well-furnished','well-Furnished'),('semi-furnished','Semi-Furnished'),('not-furnished','Not-Furnished')]
    )
    room_type = fields.Selection(
        string="Room Type",
        selection = [('1-rk','1-RK'),('1-bhk','1-BHK'),('2-bhk','2-BHK'),('3-bhk','3-BHK')],
        required = True
    )
    # purpose = fields.Selection(
    #     string="Purpose",
    #     selection = [('lender','Lender'),('reciever','Reciever')],
    #     required = True
    # )
    state = fields.Selection(
        string="state",
        selection = [('new','New'),('confirm','Confirm'),('done','Done')]
    )

    
    