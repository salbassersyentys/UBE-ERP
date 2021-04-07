# -*- coding: utf-8 -*-

{
    'name': 'Sales - External Salesperson',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'Allows to associate salesperson without extra licence',
    'description': """
# How To use

1. Go to the contact form
2. Check "Is external salesperson"
3. Grant portal access to this contact
    """,
    'depends': ['sale'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False
}
