from odoo import models, fields


class Publisher(models.Model):
    _name = "library.publisher"
    _description = "Publisher"
    _rec_name = "f_name"

    f_name = fields.Char(string="First Name", required=True)
    l_name = fields.Char(string="Last Name", required=True)
    date_join = fields.Date()
    active = fields.Boolean(default=True)
    national_id = fields.Char(string="National ID")
    image = fields.Binary()
    book_ids = fields.One2many('library.book', 'publisher_id')
