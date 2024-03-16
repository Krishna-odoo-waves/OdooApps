########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
{
    "name": "Select Category On Multiple Products",
    "summary": """Select The Category On Multiple Products In Direct/Easy Way""",
    "category": "All",
    "version": "17.0.1.0.0",
    "sequence": 2,
    "author": "Odoo Waves",
    "license": "LGPL-3",
    "website": "",
    "description": """Select Category On Multiple Products""",
    "depends":['product'],
    "data": [
        'security/ir.model.access.csv',
        'views/ow_product_inherit.xml',
        'wizards/ow_add_category_view.xml',
    ],
    "images": ['static/description/banner.gif'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price":5,
    "currency":'USD',
    "pre_init_hook": "pre_init_check",
}
