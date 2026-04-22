from odoo import api, fields, models

class SaleWizard(models.TransientModel):
    _name = "academy.sale.wizard"
    _description = "Wizard: Quick create orders for session students."

    # The session we are working with
    session_id = fields.Many2one(
        comodel_name="academy.session", 
        string="Session", 
        required=True
    )

    # The list of students who will receive a Sales Order
    student_ids = fields.Many2many(
        comodel_name="res.partner", 
        string="Students for Sale Order"
    )

    # This "reaches through" the session to find the actual Product Variant to sell
    session_product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product to Sell",
        related="session_id.course_id.product_id.product_variant_id"
    )

    def create_sale_orders(self):
        return True