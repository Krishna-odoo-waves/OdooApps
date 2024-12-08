########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import fields, models

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    ow_image_128 = fields.Image(related='product_id.image_128', string='Image')
