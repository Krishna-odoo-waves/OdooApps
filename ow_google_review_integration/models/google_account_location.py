########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import models, fields, api
import logging


class GoogleAccountLocation(models.Model):
    _name = 'google.account.location'
    _description = "Google Account ocation"

    name = fields.Char(string="Name")
    title = fields.Char(string="Title")
    review_integration_id = fields.Many2one("google.review.integration", string="Integration")
    last_updated_date = fields.Datetime("Last Review Sync Date")
    is_added = fields.Boolean(string="Field Added", default=False)

    def add_location(self):
        for rec in self:
            if rec.review_integration_id:
                rec.is_added = True
                rec.review_integration_id.location_id = [(fields.Command.link(rec.id))]

    def remove_location(self):
        for rec in self:
            if rec.review_integration_id:
                rec.is_added = False
                rec.review_integration_id.location_id = [(fields.Command.unlink(rec.id))]