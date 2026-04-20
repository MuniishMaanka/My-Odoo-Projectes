# from odoo import http


# class AcademySale(http.Controller):
#     @http.route('/academy_sale/academy_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy_sale/academy_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy_sale.listing', {
#             'root': '/academy_sale/academy_sale',
#             'objects': http.request.env['academy_sale.academy_sale'].search([]),
#         })

#     @http.route('/academy_sale/academy_sale/objects/<model("academy_sale.academy_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy_sale.object', {
#             'object': obj
#         })

