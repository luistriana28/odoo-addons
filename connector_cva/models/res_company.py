# © <2019><Luis Triana><Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    cva_user = fields.Char()
    cva_group = fields.Many2many('cva.group')
    cva_main_location = fields.Many2one('stock.location')
