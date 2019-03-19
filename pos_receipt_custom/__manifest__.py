# -*- coding: utf-8 -*-
{
    'name': "POS receipt custom",
    'summary': """
       Customize Pos receipt""",
    'description': """
        Customize Pos receipt
    """,
    'author': "Aimé Jules Andrinirina",
    'website': "",
    'category': 'Point Of Sale',
    'version': '12.0.1.0',
    'depends': [
        'base',
        'point_of_sale',
    ],
    'data': ['views/assets.xml'],
    'qweb': ['static/src/xml/pos.xml'],
}
