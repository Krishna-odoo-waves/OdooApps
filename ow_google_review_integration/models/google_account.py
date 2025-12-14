########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import models, fields, api

class GoogleAccount(models.Model):
    _name = 'google.account'
    _description = "Google Account"

    name = fields.Char(string="Name")
    account_name = fields.Char(string="Account")
    role = fields.Char(string="Role")