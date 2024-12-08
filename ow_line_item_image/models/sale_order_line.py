########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    ow_image_128 = fields.Image(related='product_id.image_128', string='Image')

    is_enable_image_field = fields.Boolean(string='Is Enable Image Field', compute='compute_enable_image_field',)

    def compute_enable_image_field(self):
        value = self.env['ir.config_parameter'].get_param('ow_line_item_image.add_so_line_image')
        for record in self:
            record.is_enable_image_field = bool(value)
        