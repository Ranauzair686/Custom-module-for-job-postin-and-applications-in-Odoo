from odoo import models, fields

class RefuseReason(models.Model):
    _name = 'refuse.reason'
    _description = 'Refuse Reason'

    name = fields.Char(string='Reason', required=True)
    
    
    
    

