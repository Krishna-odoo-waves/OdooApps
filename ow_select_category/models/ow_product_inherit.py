########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import api, fields, models,_

class ProductTemplateInherit(models.Model):
    _inherit = ['product.template']


    def add_category(self):
        return {
            'name': _('Add Cateogry To Multiple Product Templates'), 
            'type': 'ir.actions.act_window',
            'res_model': 'add.categories',
            'view_mode': 'form',   	
            'target': 'new'
        }
    
class ProductProductInherit(models.Model):
    _inherit = ['product.product']


    def add_category(self):
        return {
            'name': _('Add Cateogry To Multiple Product Variants'), 
            'type': 'ir.actions.act_window',
            'res_model': 'add.categories',
            'view_mode': 'form',   	
            'target': 'new'
        }