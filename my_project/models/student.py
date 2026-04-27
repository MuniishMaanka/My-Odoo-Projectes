from odoo import models, fields

class Student(models.Model):
    _name = 'student.record'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")