from odoo import http

class Academy(http.Controller):

    @http.route('/hello_world/', auth='public', website=True, sitemap=True)
    def hello_world(self, **kw):
        return 'Hello World!'

    @http.route('/academy/courses', auth='public', website=True, sitemap=True)
    def courses(self, **kw):
        # Fetch all courses from the database
        courses = http.request.env['academy.course'].search([])
        # Render the template and pass the 'courses' variable to it
        return http.request.render('academy.course_website', {
            'courses': courses,
        })