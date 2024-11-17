########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################

from odoo import api, fields, models

class AddCategory(models.TransientModel):
    _name = 'add.categories'
    _description = 'Add Category'
    
    category_id = fields.Many2one(
        string='Category',
        comodel_name='product.category',
    )

    def waves_add_category(self):
        return self.env[self._context.get('active_model')].browse(self._context.get('active_ids')).write({'categ_id':self.category_id.id})
    