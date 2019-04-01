# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'POS receipt custom',
    'summary': 'Customize Pos receipt',
    'version': '12.0.1.0.0',
    'category': 'POS',
    'website': 'https://odoo-community.org/',
    'author': 'Aimé Jules Andrinirina, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'depends': [
        'base',
        'point_of_sale'
    ],
    'data': [
        'views/assets.xml',
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/pos.xml',
    ]
}
