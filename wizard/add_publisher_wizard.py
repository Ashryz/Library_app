from odoo import models, fields


class AddPublisher(models.TransientModel):
    _name = "publisher.wizard"
    _description = "Add publisher wizard"

    publisher_id = fields.Many2one("library.publisher", required=True)
    book_id = fields.Many2one("library.book")

    def action_add_publisher(self):
        self.book_id.publisher_id = self.publisher_id.id
