# -*- coding: utf-8 -*-

from odoo import models , fields,api
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta
from odoo.tools.float_utils import float_compare


class rentReciever(models.Model):
    _name = "rent.reciever"
    _description = "Searching home for living"
    _sql_constraints = [
        ("check_contact_no", "CHECK(contact_no != 10)", "Please enter correct contact number")]
    _inherit = ['mail.thread','mail.activity.mixin']
     
    name = fields.Char(required = True,default="Name")
    description = fields.Text()
    renting_price = fields.Float()
    sharing = fields.Integer()
    location = fields.Text()
    bachelors = fields.Boolean()
    deposit_money = fields.Float()
    total_price = fields.Float(compute ="_compute_total_price_")
    date_availability = fields.Date(default=lambda self:fields.Datetime.today()+relativedelta(months=3))
    contact_no = fields.Integer()
    room_type = fields.Selection(
        string="Room Type",
        selection = [('1-rk','1-RK'),('1-bhk','1-BHK'),('2-bhk','2-BHK'),('3-bhk','3-BHK')]
    )
    state = fields.Selection(
        string = "Type",
        selection = [('new','New'),('confirm','Confirm'),('done','Done'),('buy','Buy'),('cancel','Cancel')],
        tracking=True
    )
    tags_ids = fields.Many2many("rent.tags",string="tags")
    offer_ids = fields.One2many("rent.offer","rents_id",string = "Offer id" )
    rent_type_id = fields.Many2one("rent.type",string = "Rent Type")
    salesperson_id = fields.Many2one("res.users",string="Sales Person")
    buyers_id = fields.Many2one("res.partner",string="Buyer")
    
    
    @api.depends('renting_price','deposit_money')
    def _compute_total_price_(self):
        for record in self:
            record.total_price = record.renting_price+record.deposit_money
    
    def action_buy(self):
        for record in self:
            if record.state=='buy':
                raise UserError("Cancel Properties cannot be buy")
            else:
                record.state='cancel'
        return True
    
    def action_cancel(self):
        for record in self:
            if record.state=='cancel':
                raise UserError("Bought properties cannot be cancel")
            else:
                record.state='buy'
        return True
    
    # @api.constrains('contact_no')
    # def _check_contact_no(self):    
    #     for rec in self:
    #         if len(str(rec.contact_no))!=10:
    #             raise ValidationError("Please enter correct number")
    #         else:
    #             return False
    #     return True
                