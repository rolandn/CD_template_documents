# -*- coding: utf-8 -*-
# Copyright 2018 Roland NEYRINCK
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "Facture custom pour Casa Domotic",
    'version': '10.0.1',
    'category': 'Generic Modules/Accounting',
    'author':   "Roland NEYRINCK",
    'website': '',
    'license': 'AGPL-3',
    "depends": [
        'account','sale',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/Facture_CD.xml',
        'views/invoice_form_CD_inherited.xml',
        'views/invoice_supplier_inherit.xml',
        'views/partner_inherit.xml'
    ],

    'installable': True,
}
