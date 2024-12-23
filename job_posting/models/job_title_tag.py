from odoo import models, api, fields

class JobtitleTag(models.Model):
    _name = 'jobtitle.tag'
    _description = 'Job Title Tags'
    
    name = fields.Char(string='Job Titles', required=True)