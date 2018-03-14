# -*- coding: utf-8 -*-
{
    'name': "Campos para contactoss",

    'summary': """
        Agregado de campos para los contactos
        """,

    'description': """
        Agregado de campos al modelo res.partner para obtener datos importantes
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/campo_codigo_cliente_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
