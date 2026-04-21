# from odoo import http


# class AcademyWebsite(http.Controller):
#     @http.route('/academy_website/academy_website', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy_website/academy_website/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy_website.listing', {
#             'root': '/academy_website/academy_website',
#             'objects': http.request.env['academy_website.academy_website'].search([]),
#         })

#     @http.route('/academy_website/academy_website/objects/<model("academy_website.academy_website"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy_website.object', {
#             'object': obj
#         })

