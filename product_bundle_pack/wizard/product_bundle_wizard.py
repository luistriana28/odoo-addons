# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class bi_wizard_product_bundle(models.TransientModel):
    _name = 'wizard.product.bundle.bi'

    product_id = fields.Many2one('product.product',string='Bundle',required=True)
    product_qty = fields.Integer('Quantity',required=True ,default=1)
    product_price = fields.Float(string="Price")
    pack_ids = fields.One2many('product.pack', related='product_id.pack_ids', string="Select Products")
    

    @api.multi
    def button_add_product_bundle_bi(self):
        
        for pack in self:
            if pack.product_id.is_pack:
                test = self.env['sale.order.line'].create({'order_id':self._context['active_id'],
                                                'product_id':pack.product_id.id,
                                                'name':pack.product_id.name,
                                                'price_unit':self.product_price,
                                                'product_uom':pack.product_id.uom_id.id,
                                                'product_uom_qty': self.product_qty
                                                })
        return True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         


    @api.onchange('product_id')
    def onchange_product(self):
        if self.product_id:
            self.product_price = self.product_id.lst_price
        else:
            pass