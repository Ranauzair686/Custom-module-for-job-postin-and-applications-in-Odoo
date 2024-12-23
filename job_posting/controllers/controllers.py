from odoo import http ,_
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug
import base64

class JobPostWebsite(http.Controller):
    @http.route('/job', type='http', auth='public', website=True)
    def jobs_list(self, **kw):
        # all_jobs = request.env['job.posting'].search([]) 
        # for job in all_jobs:
        #     print(f"Job: {job.name_id}, Published: {job.website_published}") 
        jobs = request.env['job.posting'].search([('website_published', '=', True)])
        return request.render('job_posting.index', {
            'jobs': jobs
        })
        
        
    @http.route('''/job/detail/<model("job.posting"):job>''', type='http', auth="public", website=True, sitemap=True)
    def jobs_detail(self, job, **kwargs):
        return request.render("job_posting.detail", {
            'job': job,
            'main_object': job,
        })
        
    @http.route('''/job/apply/<model("job.posting"):job>''', type='http', auth="public", website=True, sitemap=True)
    def jobs_apply(self, job, **kwargs):
        error = {}
        default = {}
        if 'website_hr_recruitment_error' in request.session:
            error = request.session.pop('website_hr_recruitment_error')
            default = request.session.pop('website_hr_recruitment_default')
        return request.render("job_posting.apply", {
            'job': job,
            'error': error,
            'default': default,
        })
        

    @http.route('/job/application/submit', auth='public', type='http', methods=['POST'], csrf=False)
    def job_application_submit(self, **kwargs):
        position_id = kwargs.get('position_id')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        linkedin_profile = kwargs.get('linkedin_profile')
        short_introduction = kwargs.get('short_introduction')
        document =  kwargs.get('document') 
        document_data = document.read()
        document_name = document.filename
        
        application = request.env['job.applicant'].create({
            'name': name,
            'email': email,
            'phone': phone,
            'position_id': position_id,
            'linkedin_profile' : linkedin_profile,
            'short_introduction' : short_introduction,
            'document' : base64.b64encode(document_data).decode("utf-8"),
            'document_name' : document_name,
        })

        return request.redirect('/job-thank-you')

    