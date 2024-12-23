from odoo import models, api, fields

class ApplicantStage(models.Model):
    _name = "applicant.stage"
    _inherit = ['mail.thread']
    
    name = fields.Char(string="Stage Name" , tracking=True)
    sequence = fields.Integer(string="Sequence", default=1 , tracking=True)