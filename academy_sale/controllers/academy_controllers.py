from odoo import http

class Academy(http.Controller):

    @http.route('/hello_world/', auth='public', website=True, sitemap=True)
    def hello_world(self, **kw):
        return 'Hello World!'