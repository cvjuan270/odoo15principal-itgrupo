from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class StockMove(models.Model):
    _inherit = 'stock.move'
    

    employee_dni = fields.Char('D.N.I.')