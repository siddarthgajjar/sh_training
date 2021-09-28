# -*- coding: utf-8 -*-

{
    'name': 'Open Academy',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module to manage training:
        - Courses
        - Sessions
        - Attendees 
    """,
    
    'author': 'Daniel Jansen',
    
    'category': 'Technical Training',
    'version': '0.1',
    
    'depends': ['sale', 'website'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_order_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizards/sale_wizard_view.xml',
        'reports/session_report_template.xml',
        'views/academy_web_templates.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ],
}