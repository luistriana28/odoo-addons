# © <2018> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CvaGroup(models.Model):
    _name = 'cva.group'
    _description = 'group of CVA'
    _order = 'name'

    name = fields.Char(required=True)
