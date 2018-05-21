# -*- coding: utf-8 -*-
{
    'name': "Edición de facturas",

    'summary': """
        Edición de la vista de arbol de las facturas
        """,

    'description': """
        Agregado empresa o compañia relacionada en las facturas del cliente
    """,

    'author': "Soluciones4G OGM",
    'website': "http://www.soluciones4g.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'base',
        'account_accountant',
        'edicion_contactos',
    ],

    'data': [
        'views/empresa_enfacturacion_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
