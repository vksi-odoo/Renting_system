# -*- coding: utf-8 -*-

from odoo import models, fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class pg(models.Model):
    _name = "pg.pg"
    _description = "This is Paying Guest model"
    _order = "id desc"
    _inherit = ['mail.thread','mail.activity.mixin']
    
    name = fields.Char(required=True,default="Name")
    description = fields.Text("Description",copy=False,default="What is your furthur requirment?")
    date_availability = fields.Date(default = lambda self: fields.Datetime.today()+relativedelta(months=3))
    pg_price = fields.Float(compute='_compute_sharing_')
    sharing = fields.Selection(
        string="Room sharing",
        selection=[('single_bed','Single Sharing'),
                   ('double_sharing','Double Sharing'),
                   ('triple_sharing','Triple Sharing'),
                   ('quadruple_sharing','Quadruple Sharing'),('quintuple_sharing','Quintuple Sharing')],
    )
    location = fields.Text()
    deposit_money = fields.Float(compute='_compute_sharing_')
    total_price = fields.Float(compute="_compute_total_price_")
    contact_no = fields.Integer()
    food_category = fields.Selection(
        string = "Food Category",
        selection = [('vegetarian','Vegetarian'),('non-vegetarian','Non-Vegetarian')]
    )
    state = fields.Selection(
        string = "Type",
        selection = [('new','New'),('confirm','Confirm'),('done','Done'),('cancel','Cancel')],
        default="new",
        tracking=True
    )
    tags_ids = fields.Many2many("rent.tags",string="tags")
    offer_ids = fields.One2many("rent.offer","pg_id",string = "Offer id" )
    salesperson_id = fields.Many2one("res.users",string="Sales Person")
    buyers_id = fields.Many2one("res.partner",string="Buyer")
    
    @api.depends('sharing','pg_price','deposit_money')
    def _compute_sharing_(self):
        for rec in self:
            if rec.sharing == "single_bed":
                rec.pg_price = 10000
                rec.deposit_money = 5000
            elif rec.sharing == "double_sharing":
                rec.pg_price = 8000
                rec.deposit_money = 4000
            elif rec.sharing == "triple_sharing":
                rec.pg_price = 6500
                rec.deposit_money = 3000
            elif rec.sharing == "quadruple_sharing":
                rec.pg_price = 5000
                rec.deposit_money = 2500
            elif rec.sharing == "quintuple_sharing":
                rec.pg_price = 5000
                rec.deposit_money = 2000
            else:
                rec.pg_price = 0
                rec.deposit_money = 0
    
    @api.depends('pg_price','deposit_money')
    def _compute_total_price_(self):
        for record in self:
            record.total_price = record.pg_price+record.deposit_money
            
    def action_done(self):
        for record in self:
            if record.state=='cancel':
                raise UserError("Cancel PG cannot be accepted")
            else:
                record.state='done'
        return True
    
    def action_cancel(self):
        for record in self:
            if record.state=='done':
                raise UserError("Accepted PG cannot be cancel")
            else:
                record.state='cancel'
        return True
    
    