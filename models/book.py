from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = "library.book"
    _description = "Book"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    seq = fields.Char(default='New')
    code = fields.Char(required=True)
    active = fields.Boolean(default=True)
    publish_date = fields.Date()
    image = fields.Binary()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('published', 'Published')
    ], default='draft')
    publisher_id = fields.Many2one('library.publisher')
    line_ids = fields.One2many("library.book.line", "book_id")

    @api.constrains("publisher_id")
    def _check_publisher_id(self):
        for rec in self:
            if not rec.publisher_id:
                raise ValidationError("Publisher is required")

    @api.model
    def create(self, vals_list):
        res = super(Book, self).create(vals_list)
        res.seq = self.env['ir.sequence'].next_by_code('book_seq')
        return res

    @api.model
    def archive_book(self):
        book_ids = self.search([])
        for book in book_ids:
            if book.state == 'draft':
                book.active = False

    def action_add_publisher(self):
        action = self.env['ir.actions.actions']._for_xml_id('library_app.publisher_wizard_action')
        action['context'] = {
            'default_book_id': self.id
        }
        return action

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_published(self):
        for rec in self:
            rec.state = 'published'

    def server_published_state(self):
        for rec in self:
            rec.state = 'published'


class BookLine(models.Model):
    _name = "library.book.line"
    _description = "Book Line"

    name = fields.Char()
    date = fields.Date()
    description = fields.Char()
    book_id = fields.Many2one("library.book")
