########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
{
    "name": "App & Settings Shortcut",
    "summary": """By providing instant access to both apps and their configurations, the module empowers users to focus on their tasks without interruptions.""",
    "category": "All",
    "version": "18.0.1.0.0",
    "sequence": 2,
    "author": "Odoo Waves",
    "license": "LGPL-3",
    "website": "",
    "description": """With the Quick Access App & Settings module, you can access any app and its settings directly from anywhere in Odoo without needing to navigate back to the main app or settings menu.""",
    "depends":['web'],
    'assets': {   
            'web.assets_backend': [      
            'ow_app_setting_shortcut/static/src/js/systray_icon.js', 
            'ow_app_setting_shortcut/static/src/xml/systray_icon.xml', 
            'ow_app_setting_shortcut/static/src/css/extra_style.css'
            
            ]
    },
    "images": ['static/description/banner.gif'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price":2,
    "currency":'USD',
    "pre_init_hook": "pre_init_check",
}
