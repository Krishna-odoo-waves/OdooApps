########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
{
    "name": "Line Item Image for Sale|Invoice|Purchase",
    "summary": """Display product images directly in the Sale Order, Invoice, and Purchase Order lines to enhance visibility and improve the user experience.""",
    "category": "All",
    "version": "18.0.1.0.0",
    "sequence": 2,
    "author": "Odoo Waves",
    "license": "LGPL-3",
    "website": "",
    "description": """The Line Item Image for Sale, Invoice, and Purchase Order Lines module provides a simple but powerful enhancement to Odoo's standard order and invoice views. By displaying product images within the line items of Sales Orders, Invoices, and Purchase Orders, this module makes it easier for users to recognize products at a glance.""",
    "depends":['sale','purchase','account'],
    "data": [
        'views/sale_order_views.xml',
        'views/purchase_order_view.xml',
        'views/account_move_view.xml',
    ],
    "images": ['static/description/banner.gif'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price":2,
    "currency":'USD',
    "pre_init_hook": "pre_init_check",
}
