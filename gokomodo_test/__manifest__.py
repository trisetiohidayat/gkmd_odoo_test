# -*- coding: utf-8 -*-
{
    'name': "gokomodo_test",

    'summary': """
        Gokomodo Business Model Test""",

    'description': """
        This module to add categorization by business models in sale order and tax.
    """,

    'author': "Tri Setio Hidayat",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale','account'],

    'data': [
        'security/ir.model.access.csv',
        'data/business_model_data.xml',
        'views/business_model_views.xml',
        'views/sale_order_views.xml',
        'views/account_tax_views.xml',
        'views/res_config_settings_views.xml',
    ],
}
