from odoo import models, api, fields
from odoo.exceptions import ValidationError


class JobPosting(models.Model):
    _name = 'job.posting'
    _inherit = ['mail.thread']
    _description = 'Job Posting'
    
    name_id = fields.Many2one('jobtitle.tag' , string='Job Title' , required=True , tracking=True)
    description = fields.Html(string='Job Description', tracking=True)
    requirements = fields.Html(string='Job Requirements', tracking=True)
    location =  fields.Selection([
        ('onsite' , 'Onsite'),
        ('remote' , 'Remote'),
        ('hybrib' , 'Hybrid')
    ], string = 'Job Location' , default = 'onsite', tracking=True)
    
    open_positions = fields.Char(string="Open Positions" , tracking=True , required=True)
    job_status =  fields.Selection([
        ('open' , 'Open'),
        ('closed' , 'Closed')
    ], string="Job Status" , default='open' , required=True , tracking =True)
    job_type = fields.Selection([
        ('full_time' , 'Full Time'),
        ('part_time' , 'Part Time'),
        ('contract'   , 'Contract'),
        ('internship' , 'Internship')
    ], string='Employment Type' , default = 'full_time', tracking=True)
    
    salary = fields.Float(string='Salary', tracking=True)
    experience = fields.Selection([
        ('fresh' , 'Fresh'),
        ('junior' , 'Junior'),
        ('midsenior' , 'Mid Senior'),
        ('senior' , 'Senior')
    ], string = 'Experience' , default = 'junior', tracking=True)
    
    skills_ids = fields.Many2many('job.tag', string="Required Skills", tracking=True)
    website_published = fields.Boolean(string="Is Published" , tracking=True)
    
    
    
    # yeh function override kare ga default name_get method ko taake hmaare url men jobname-job id is format men ayeee 
    def name_get(self):
        result = []
        for record in self:
            if record.name_id:
                result.append((record.id, record.name_id.name))
            else:
                result.append((record.id, "Unnamed Job Posting"))  
        return result
    
    

    

        
        

        
    