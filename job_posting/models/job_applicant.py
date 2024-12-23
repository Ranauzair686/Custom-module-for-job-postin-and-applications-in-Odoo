from odoo import models, api, fields
from odoo.exceptions import ValidationError


AVAILABLE_PRIORITIES = [
    ('0', 'Poor'),
    ('1', 'Average'),
    ('2', 'Good'),
    ('3', 'Very Good'),
    ('4', 'Excellent'),
    ('5', 'Super Excellent')
]
# Job applicant model 
class JobApplicant(models.Model):
    _name = "job.applicant"
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _description = "Job Applicantions"
    _rec_names_search = ['reference', 'name' ,'position_id']
    
    name = fields.Char(string="Applicant's Name", required=True, tracking=True)
    email =fields.Char(string="Email" , required=True , tracking=True)
    phone = fields.Char(string="Phone Numbere" , required=True , tracking=True)
    position_id = fields.Many2one('job.posting' , string="Applied Job" , required=True)
    document = fields.Binary(string="Resume")
    document_name = fields.Char(string="File Name")
    linkedin_profile = fields.Char(string="LinkedIn Profile" , required=True)
    short_introduction = fields.Text(string="Short Introduction" , required=True)
    reference = fields.Char(string="Reference" ,  tracking=True , default='New')
    first_interview_remarks = fields.Selection(AVAILABLE_PRIORITIES, string="First Interview Remarks", default='0')
    second_interview_remarks = fields.Selection(AVAILABLE_PRIORITIES, string="Second Interview Remarks", default='0')
    application_stage = fields.Selection([
        ('initialqualificaton', 'Initial Qualification') , ('firstinterview' , 'First Interview') , ('secondinterview' , 'Second Interview') , ('contractproposal' , 'Contract Proposal') , ('contractsigned' , 'Cntract Signed') , ('refused' , 'Refused') 
    ], tracking= True)
    first_interview_time= fields.Char(string="First Interview Time" , tracking= True)
    first_interview_date = fields.Date(string="First Interview Date" , tracking= True)
    second_interview_time = fields.Char(string="Second Interview Time " , tracking= True)
    second_interview_date = fields.Date(string="Second Interview Date" , tracking= True)
    refuse_reason_id = fields.Many2one('refuse.reason', string='Refuse Reason' , tracking= True)
    salary_expected = fields.Float(string="Expected Salary" , tracking= True)
    salary_proposed = fields.Float(string="Proposed Salary" , tracking= True)
    interviewer  =  fields.Char(string="Interviewer" ,tracking= True) 
    
    
    
    
    # create the refrence no for the every application
    @api.model_create_multi
    def create(self , vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals ['reference'] == 'New':
                vals ['reference'] = self.env ['ir.sequence'].next_by_code('job.applicant')
        return super(). create(vals_list)
    
    # action for the staus bar 
    def action_refuse(self):
        for rec in self:
            rec.application_stage = "refused"
        

    # function for checking the tinme format wether it is true or not 
    @api.constrains('first_interview_time', 'second_interview_time')
    def _check_time(self):
        for record in self:
            if record.first_interview_time:
                start, end = self._parse_time(record.first_interview_time)
                if start >= end:
                    raise ValidationError("First interview start time must be earlier than the end time.")
            if record.second_interview_time:
                start, end = self._parse_time(record.second_interview_time)
                if start >= end:
                    raise ValidationError("Second interview start time must be earlier than the end time.")

    def _parse_time(self, time):
        """Parses a time range string like '7:00 PM - 7:30 PM' into two datetime.time objects."""
        import datetime
        try:
            start_str, end_str = time.split('-')
            start = datetime.datetime.strptime(start_str.strip(), "%I:%M %p").time()
            end = datetime.datetime.strptime(end_str.strip(), "%I:%M %p").time()
            return start, end
        except ValueError:
            raise ValidationError("Time range format should be 'HH:MM AM/PM - HH:MM AM/PM'.")


   
    