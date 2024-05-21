from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = "library.book"
    _description = "Book"

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    active = fields.Boolean(default=True)
    publish_date = fields.Date()
    image = fields.Binary()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('published', 'Published')
    ])
    publisher_id = fields.Many2one('library.publisher')

    @api.constrains("publisher_id")
    def _check_publisher_id(self):
        for rec in self:
            if not rec.publisher_id:
                raise ValidationError("Publisher is required")

    def action_add_publisher(self):
        action = self.env['ir.actions.actions']._for_xml_id('library_app.publisher_wizard_action')
        action['context'] = {
            'default_book_id': self.id
        }
        return action
