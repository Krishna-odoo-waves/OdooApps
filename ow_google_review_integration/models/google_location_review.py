########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import models, fields, api

class GoogleLocationReview(models.Model):
    _name = 'google.location.review'
    _description = "Google Location Review"

    name = fields.Char(string="Name")
    reviewId = fields.Char(string="Review Id")
    rating = fields.Char(string="Rating")
    comment = fields.Char(string="Review Comment")
