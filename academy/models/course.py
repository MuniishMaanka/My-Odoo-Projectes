from odoo import api, fields, models

class Course(models.Model):
    _name = "academy.course"
    _description = "Course Info"

    # Reserved Fields
    name = fields.Char(string='Title', required=True)
    active = fields.Boolean(string='Active', default=True)

    # Simple Fields
    description = fields.Text(string='Description')
    level = fields.Selection(string='Level',
                             selection=[('beginner', 'Beginner'),
                                        ('intermediate', 'Intermediate'),
                                        ('advanced', 'Advanced')],
                             copy=False)

    # Relationship Field
    session_ids = fields.One2many(
        comodel_name="academy.session", 
        inverse_name="course_id", 
        string="Sessions"
    )