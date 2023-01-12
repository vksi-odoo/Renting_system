# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta
from odoo.tools.float_utils import float_compare

class rentLender(models.Model):
    _name = "rent.lender"
    _description = "Giving my room for rent"
    _sql_constarins=[('check_contact_no','CHECK(contact_no!=10)','Please enter correct number')]
    _inherit = ['mail.thread','mail.activity.mixin']
    
    name = fields.Char(required=True,default="Name")
    description = fields.Text("Description",copy=False,default="What is your furthur requirment?")
    date_availability = fields.Date(default = lambda self: fields.Datetime.today()+relativedelta(months=3))
    renting_price = fields.Float()
    sharing = fields.Integer()
    location = fields.Text()
    bachelors = fields.Boolean(default = True)
    deposit_money = fields.Float()
    contact_no = fields.Integer()
    total_price = fields.Float(compute="_compute_total_price_")
    
    room_type = fields.Selection(
        string="Room Type",
        selection = [('1-rk','1-RK'),('1-bhk','1-BHK'),('2-bhk','2-BHK'),('3-bhk','3-BHK')],
    )
    # purpose = fields.Selection(
    #     string="Purpose",
    #     selection = [('lender','Lender'),('reciever','Reciever')],
    #     required = True
    # )
    state = fields.Selection(
        string="state",
        selection = [('new','New'),('confirm','Confirm'),('done','Done'),('sold','Sold'),('cancel','Cancel')]
    )
    tags_ids = fields.Many2many("rent.tags",string="tags")
    offer_ids = fields.One2many("rent.offer","rent_id",string="offer ids")
    rent_type_id = fields.Many2one("rent.type",string = "Rent Type")
    salesperson_id = fields.Many2one("res.users",string="Sales Person")
    buyers_id = fields.Many2one("res.partner",string="Buyer")
    
    @api.depends('renting_price','deposit_money')
    def _compute_total_price_(self):
        for record in self:
            record.total_price = record.renting_price+record.deposit_money
            
    def action_sold(self):
        for record in self:
            if record.state== 'cancel':
                raise UserError("Cancel propertes cannot be sold")

            else:
                record.state='sold' 
        return True
    
    def action_cancel(self):
        for record in self:
            if record.state=='sold':
                raise UserError("Sold properties cannot be cancel")
            else:
                record.state='cancel'
        return True  
    
    @api.constrains('contact_no')
    def _check_contact_no(self):
        for rec in self:
            if len(str(rec.contact_no))!=10:
                raise UserError("Please enter correct number")   
            else:
                return False
        return True
    

    
    