########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    ow_image_128 = fields.Image(related='product_id.image_128', string='Image')
