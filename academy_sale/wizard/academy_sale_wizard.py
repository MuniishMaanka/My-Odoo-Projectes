from odoo import api, fields, models

class SaleWizard(models.TransientModel):
    _name = "academy.sale.wizard"
    _description = "Wizard: Quick create orders for session students."

    def _default_session(self):
        # Automatically detects the session from the view the user is coming from
        return self.env["academy.session"].browse(self._context.get("active_id"))

    session_id = fields.Many2one(
        comodel_name="academy.session", 
        string="Session", 
        required=True, 
        default=_default_session
    )

    # NEW: Shows the students currently in the session (Read-only reference)
    session_student_ids = fields.Many2many(
        comodel_name="res.partner", 
        string="Students in current session", 
        related="session_id.student_ids", 
        help="This are the student currently enrolled in the session."
    )

    # The list of students the admin actually selects to create orders for
    student_ids = fields.Many2many(
        comodel_name="res.partner", 
        string="Students for Sale Order"
    )

    session_product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product to Sell",
        related="session_id.course_id.product_id.product_variant_id"
    )

    def create_sale_orders(self):
        return True