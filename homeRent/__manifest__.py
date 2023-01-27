# -*- coding: utf-8 -*-
{
    'name' : 'Rent System',
    'description' : 'Home renting system',
    'data' : [
        'security/ir.model.access.csv',
        'views/rent_action_menu.xml',
        'views/rent_lender_views.xml',
        'views/rent_system_views.xml',
        'views/rent_reciever_views.xml',
        'views/rent_type_views.xml',
        'views/rent_offer_views.xml',
        'views/rent_tags_views.xml',
        'views/res_users_views.xml',
        'views/pg_views.xml'
        ],
    # 'demo' : [
    #   'demo/demo_data.xml'  
    'depends': ['base','mail'],
    'application' : True,
}