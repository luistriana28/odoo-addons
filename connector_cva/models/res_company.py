# © <2019><Luis Triana><Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
import requests
import xml.etree.ElementTree as ET
import base64


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    cva_user = fields.Char()
    cva_group = fields.Many2many('cva.group')
    cva_main_location = fields.Many2one('stock.location')

    @api.multi
    def connect_cva(self, params):
        # Connect to CVA web-services
        # @param params: dict with parameters to generate xml file
        # @return: returns a xml object
        url = (
            'https://www.grupocva.com/catalogo_clientes_xml/lista_precios.xml')
        data = requests.get(
            (url), params=params).content
        connection = ET.fromstring(data)
        return connection

    @api.multi
    @api.depends('cva_user', 'cva_main_location')
    def get_groups(self):
        group = self.cva_group
        group_list = [x.name for x in group.search([])]
        params = {'cliente': self.cva_user}
        connection = self.connect_cva(params)
        for item in connection.filtered(lambda c: c.connection):
            if (item.findtext('grupo') not in group_list and
                    item.findtext('grupo') != ''):
                group.create({'name': item.findtext('grupo')})
                group_list.append(item.findtext('grupo'))

    @api.multi
    def create_product(self, item):
        product_obj = self.env['product.product']
        product_tempalte_obj = self.env['product.template']
        find = item.findtext
        if not find('imagen'):
            image = False
        else:
            image = base64.b64encode(
                requests.get(find('imagen')).content)
        product = product_obj.create({
            'name': find('descripcion'),
            'default_code': find('clave'),
            'standard_price': float(find('precio')),
            'description': (
                'Group\n%s\nSubgroup\n%s\nFicha Comercial\n%s\nFicha '
                'Tecnica\n%s\n' % (find('grupo'), find('subgrupo'),
                                   find('ficha_comercial'),
                                   find('ficha_tecnica'))),
            'description_sale': find('ficha_comercial'),
            'image_medium': image,
            'type': 'product'
            })
        product_template_id = product_tempalte_obj.search([(
            'default_code', '=', product.default_code)])
        self.update_product_qty(product_template_id.id, item)

        return product_template_id

    @api.multi
    def update_product_qty(self, template_id, item):
        change_qty_wiz = self.env['stock.change.product.qty']
        product_product = self.env['product.product']
        product_template = self.env['product.template']
        main_location = self.main_location.name
        template = product_template.search([('id', '=', template_id)])
        product = product_product.search([(
            'default_code', '=', template.default_code)])
        location_ids = self.connector_cva.cva_main_location
        for location in location_ids:
            name = 'VENTAS_' + location.name
            if location.name == main_location:
                name = 'disponible'
            if item.findtext(name) != '0':
                wizard = change_qty_wiz.create({
                    'product_id': product.id,
                    'new_quantity': item.findtext(name),
                    'location_id': location.id,
                })
                wizard.change_product_qty()

    @api.model
    def update_product_cron(self):
        user_id = self.cva_user
        product = self.env['product.product']
        product_template = self.env['product.template']
        product_list = [x.default_code for x in product.search([])]
        group_list = self.env.user.company_id.cva_group
        for group in group_list:
            params = {
                'cliente': user_id,
                'grupo': group.name,
                'sucursales': '1',
                'MonedaPesos': '1',
                }
            connection = self.connect_cva(params=params)
            if connection < 1:
                pass
            for item in connection.filtered(lambda c: c.connection):
                if item.findtext('clave') in product_list:
                    product_template_id = product_template.search([
                        ('default_code', '=', item.findtext('clave'))])
                    product_id = product.search([
                        ('default_code', '=', item.findtext('clave'))])
                    product_id.standard_price = float(
                        item.findtext('precio'))
                    self.update_product_qty(product_template_id.id, item)

    @api.multi
    def get_products(self):
        product = self.env['product.product']
        group_list = [x.name for x in self.cva_group]
        product_list = [x.default_code for x in product.search([])]
        for group in group_list:
            params = {
                'cliente': self.cva_user,
                'grupo': group,
                'depto': '1',
                'dt': '1',
                'dc': '1',
                'subgpo': '1',
                'sucursales': '1',
                'MonedaPesos': '1',
            }
            connection = self.connect_cva(params)
            for item in connection.filtered(lambda c: c.connection):
                find = item.findtext
                if find('clave') not in product_list:
                    self.create_product(item)
