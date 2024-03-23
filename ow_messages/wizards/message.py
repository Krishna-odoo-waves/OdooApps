########################################################################
#                                                                      #
#     ------------------------ODOO WAVES----------------------         #
#     --------------odoowaves.solution@gmail.com--------------         #
#                                                                      #
########################################################################
from odoo import api, fields, models

class Messages(models.TransientModel):
    _name = 'message.message'
    _description = "Message Information"

    ow_message = fields.Html(
        string='Message',
    )
    
    def message_format(self,tag,message,message_tag):
        icon = False
        if tag == 'success':
            icon = '<i class="fa fa-thumbs-o-up"></i>'
        elif tag == 'info':
            icon = '<i class="fa fa-info-circle"></i>'
        elif tag == 'warning':
            icon = '<i class="fa fa-exclamation-triangle"></i>'
        elif tag == 'danger':
            icon = '<i class="fa fa-exclamation-circle"></i>'


        return f"""<div class="alert alert-{tag}" role="alert">
                    <h3 class='alert-heading'>{icon}  {message_tag} !</h3><hr>
                    {message}
                    </div>"""
    @api.model
    def success(self,message,message_tag='Success',header='Information/Summary'):
        message=self.message_format(tag='success',message=message,message_tag=message_tag)
        return self.message(message=message,header=header)
        
    @api.model
    def info(self,message,message_tag='Information',header='Information/Summary'):
        message=self.message_format(tag='info',message=message,message_tag=message_tag)
        return self.message(message=message,header=header)

    @api.model
    def warning(self,message,message_tag='Warning',header='Information/Summary'):
        message=self.message_format(tag='warning',message=message,message_tag=message_tag)
        return self.message(message=message,header=header)

    @api.model
    def error(self,message,message_tag='Error',header='Information/Summary'):
        message=self.message_format(tag='danger',message=message,message_tag=message_tag)
        return self.message(message=message,header=header)


    def message(self,message,header):
        res = self.create({'ow_message': message})
        return {
            'name'     : header,
            'type'     : 'ir.actions.act_window',
            'res_model': 'message.message',
            'view_mode': 'form',
            'target'   : 'new',
            'res_id'   : res.id,
        }
