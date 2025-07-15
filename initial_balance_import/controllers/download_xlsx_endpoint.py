from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import content_disposition
import base64


class DownloadXlsxEndpoint(http.Controller):
    @http.route('/web/download/initial_balance_template', type='http', auth="public")
    def initial_balance_template(self, **kw):
        filename = 'Plantilla Saldo Inicial.xlsx'
        invoice_xls = request.env['ir.attachment'].sudo().search([
            ('name','=','initial_balance_template.xlsx')
        ],limit=1)
        filecontent = base64.b64decode(invoice_xls.datas)
        return request.make_response(
            filecontent,
            [
                ('Content-Type', 'application/octet-stream'),
                (
                    'Content-Disposition', 
                    content_disposition(filename)
                )
            ]
        )