{
    'name' : 'Job Posting Sytem',
    'version' : '1.0.0' ,
    'summary' : 'A custom module to manage our job posting',
    'author' : 'Rana Uzair',
    'category' : 'Human Resources',
    'depends' :[
        'mail','website'
    ],
    'data' : [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/job_posting_readonlyview.xml',
        'views/applicant_stage_view.xml',
        'views/job_tag_view.xml',
        'views/job_posting_view.xml',
        'views/job_title_tag_view.xml',
        'views/job_applicantview.xml',
        'views/refuse_reason_view.xml',
        'views/menu.xml',
        'views/job_posting_template.xml',
        'views/job_applicant_template.xml',
        'views/job_detail_template.xml'
    ],
    'installable': 'True',
    'application' : 'True',
    
    'assets': {
        'web.assets_frontend': [
            'job_posting/static/src/scss/**/*',
        ],
    },
    
    
}