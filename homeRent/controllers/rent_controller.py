# -*- coding: utf-8 -*-
from odoo import http

class rent_lender(http.Controller):
   @http.route(['/homeRent/lender/','/homeRent/lender/page/<int:page>'],auth='public',website=True)
   def index(self,page=0,search='',**kw):
        domain=[]
        if search:
            domain.append(('name','ilike','search'))
        lending = http.request.env['rent.lender'].search(domain)
        total_total = lending.sudo().search_count([])
        pager = http.request.website.pager(
            url = '/homeRent/lender/',
            total = total_total,
            page=page,
            step=3,
            url_args = None
        )
        package = http.request.env['rent.lender'].search(domain,limit=4,offset=pager['offset'])
        return http.request.render('homeRent.index',{
            'properties' : package,
            'pager':pager,
        })
        
   @http.route('/homeRent/<model("rent.lender"):properties>/',auth='public',website=True)
   def property(self,properties):
        return http.request.render('homeRent.template_controller',{
            'proxy' : properties
        })        
    
class rent_lender(http.Controller):
   @http.route(['/homeRent/reciever/','/homeRent/reciever/page/<int:page>'],auth='public',website=True)
   def index(self,page=0,search='',**kw):
        domain=[]
        if search:
            domain.append(('name','ilike','search'))
        lending = http.request.env['rent.lender'].search(domain)
        total_total = lending.sudo().search_count([])
        pager = http.request.website.pager(
            url = '/homeRent/reciever/',
            total = total_total,
            page=page,
            step=3,
            url_args = None
        )
        package = http.request.env['rent.reciever'].search(domain,limit=4,offset=pager['offset'])
        return http.request.render('homeRent.indexes',{
            'properties' : package,
            'pager':pager,
        })
        
   @http.route('/homeRent/<model("rent.reciever"):propert>/',auth='public',website=True)
   def property(self,propert):
        return http.request.render('homeRent.rec_controller',{
            'pro' : propert
        })        


        
class pg_pg(http.Controller):
    @http.route(['/homeRent/pg/','/homeRent/pg/page/<int:page>'],auth='public',website=True)
    def indexes(self,page=0,search='',**kw):
        domain=[]
        if search:
            domain.append(('name','ilike','search'))
        paying = http.request.env['pg.pg'].search(domain)
        total_total = paying.sudo().search_count([])
        pager=http.request.website.pager(
            url= '/homeRent/pg/',
            total=total_total,
            page=page,
            step=3,
            url_args =None            
        )
        package = http.request.env['pg.pg'].search(domain,limit=4,offset=pager['offset'])
        return http.request.render('homeRent.pg',{
            'properties':package,
            'pager' : pager
        })
        
    @http.route('/homeRent/<model("pg.pg"):prop>/',auth='public',website=True)
    def property(self,prop):
        return http.request.render('homeRent.pg_controller',{
            'stt' : prop
        })
