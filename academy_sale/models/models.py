# from odoo import models, fields, api


# class academy_sale(models.Model):
#     _name = 'academy_sale.academy_sale'
#     _description = 'academy_sale.academy_sale'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

