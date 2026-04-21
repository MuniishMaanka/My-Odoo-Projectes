from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # In Odoo 19, the field is 'type', not 'detailed_type'
    type = fields.Selection(
        selection_add=[('course', 'Course')],
        ondelete={'course': 'set service'}
    )

    course_ids = fields.One2many(comodel_name="academy.course", inverse_name="product_id")

    def _detailed_type_mapping(self):
        # We still override the mapping to tell Odoo how 'course' behaves
        type_mapping = super()._detailed_type_mapping()
        type_mapping['course'] = 'service'
        return type_mapping