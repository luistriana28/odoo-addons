##########################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>#######################
{
    "name": "Pos All Orders List",
    "summary": "POS All Orders List model display all old orders and this model linked with POS order reprint and POS Reorder.",
    "category": "point_of_sale",
    "version": "12.0.1.0.0",
    "author": "Webkul Software Pvt. Ltd.",
    "website": "",
    "depends": ['point_of_sale'],
    "data": [
        'views/pos_orders_view.xml',
        'views/template.xml',
    ],
    "qweb": ['static/src/xml/pos_orders.xml'],
    "images": ['static/description/Banner.png'],
    "application": True,
    "installable": True,
    "auto_install": False,
    "pre_init_hook": "pre_init_check",
}
