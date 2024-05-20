from odoo import models, fields


class Book(models.Model):
    _name = "library.book"
    _description = "Book"

    name = fields.Char()
    code = fields.Char()
    active = fields.Boolean(default=True)
    publish_date = fields.Date()
    image = fields.Binary()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('published', 'Published')
    ])
