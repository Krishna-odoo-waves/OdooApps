########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
{
    "name": "Messages",
    "summary": """You Can Represent Your Custom Messages Information In Attractive/Easy Way""",
    "category": "Tool",
    "version": "17.0.1.0.0",
    "sequence": 2,
    "author": "Odoo Waves",
    "license": "LGPL-3",
    "website": "",
    "description": """From This Module Represent Your Custom Messages Information In Simple/Easy Way """,
    "depends":[
    ],
    "data": [
        'security/ir.model.access.csv',
        'wizards/message.xml',
    ],
    "images": ['static/description/banner.gif'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price":5,
    "currency":'USD',
    "pre_init_hook": "pre_init_check",
}