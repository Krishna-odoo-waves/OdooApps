########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
{
    "name": "Google Review Integration",
    'summary': 'Connect multiple Google Business accounts with Odoo to sync locations and customer reviews using scheduled cron jobs.',
    "category": "Marketing",
    "version": "19.0.1.0.0",
    "sequence": 2,
    "author": "Odoo Waves",
    "license": "LGPL-3",
    "website": "",
    'description': """
    Google Review Integration for Odoo

    This module allows you to integrate multiple Google Business accounts with Odoo and manage customer reviews in a centralized and automated way. It follows a structured workflow where Google accounts are connected first, business locations are fetched based on the selected account, and customer reviews are synchronized location-wise.

    The module uses scheduled cron jobs to automatically fetch Google Reviews at regular intervals, ensuring that review data in Odoo is always up to date without requiring manual synchronization. Reviews are stored in a structured and user-friendly format, including rating, review content and reviewer details.

    Based on predefined rules and conditions, the system can automatically reply to customer reviews, helping businesses maintain consistent and timely engagement with customers. The integration supports multiple Google accounts within a single Odoo database, making it suitable for businesses managing multiple brands or locations.

    This module helps businesses monitor customer feedback, improve online reputation management, and streamline Google Review handling directly from Odoo.
    """,

    'data':[
        'security/ir.model.access.csv',
        'data/cron.xml',
        'views/google_review_integration.xml',
        'views/google_account_view.xml',
        'views/google_location_review_view.xml',
        'views/google_account_location_view.xml',
    ],
    "images": ['static/description/banner.gif'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price":10,
    "currency":'USD',
    "pre_init_hook": "pre_init_check",
}