# © <2020><Luis Triana><Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Connector CVA",
    "summary": "Module to sync with CVA web-services",
    "license": "AGPL-3",
    "version": "12.0.0.1.0",
    "author": "Jarsa Sistemas, S.A. de C.V., Luis Triana",
    "website": "http://www.jarsa.com.mx",
    "category": "CVA connector",
    "depends": [
        'website_sale',
        'stock',
    ],
    "data": [
        'data/cva_warehouse.xml',
        'data/ir_cron_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_company_view.xml',
        'views/cva_group_view.xml',
        'views/product_template_view.xml',
    ],
    "installable": True,
}
