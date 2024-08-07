from odoo import http
from odoo.http import request


class BookApi(http.Controller):

    @http.route('/book/<int:book_id>', methods=['GET'], type='json', auth='none', csrf=False)
    def get_book_byid(self, book_id):
        res = request.env['library.book'].sudo().search([('id', '=', book_id)])
        return {
            "id": res.id,
            "name": res.name,
            "code": res.code,
            "publisher": f"{res.publisher_id.f_name} {res.publisher_id.l_name}",
        }
