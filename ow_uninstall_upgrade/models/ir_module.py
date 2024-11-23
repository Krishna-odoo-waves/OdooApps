########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import models

class IrModule(models.Model):
    _inherit = 'ir.module.module'

    def bulk_uninstall_module(self):
        installed_rec = self.filtered(lambda rec : rec.state == 'installed')
        for rec in installed_rec:
            rec.button_immediate_uninstall()
