# -*- coding: utf-8 -*-

{
    'name': "Test Module",

    'summary': """
        Testing purpose""",

    'description': """
        Test module with experimental fields from test description
        """,

    'author': "Mark0P0L0",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': "Generic Modules/Others",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/test.xml',
        # 'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],

}
