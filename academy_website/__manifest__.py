{
    'name': "academy_website",

    'author': "Odoo, Inc",
    'website': "https://www.odoo.com",

    'license': 'LGPL-3',

    'category': 'Custom Modules/Tech Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['academy', 'sale_management'],

    # always loaded
    'data': [
        'views/academy_web_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'auto_install': True,
}

