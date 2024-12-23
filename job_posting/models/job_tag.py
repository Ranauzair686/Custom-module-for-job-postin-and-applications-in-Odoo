from odoo import models, api, fields

class JobTag(models.Model):
    _name = 'job.tag'
    _description = 'Job Tags'
    
    name = fields.Char(string='Skills', required=True)