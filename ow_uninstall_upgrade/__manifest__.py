########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
{
    "name": "Uninstall/Upgrade Tool",
    "summary": """Manage your modules effortlessly by uninstalling or upgrading them directly from the Kanban view—no more digging through menus. With just a few clicks, you can streamline operations, boost productivity, and focus on what truly matters. Upgrade your workflow today!""",
    "category": "All",
    "version": "17.0.1.0.0",
    "sequence": 2,
    "author": "Odoo Waves",
    "license": "LGPL-3",
    "website": "",
    "description": """Easily uninstall or upgrade modules directly from the Kanban view with a single click. This tool simplifies module management, eliminating extra steps and saving time for Odoo users.""",
    "data": [
        'views/ir_model_view.xml',
    ],
    "images": ['static/description/banner.gif'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price":5,
    "currency":'USD',
    "pre_init_hook": "pre_init_check",
}
