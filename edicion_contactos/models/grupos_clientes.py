# -*- coding: utf-8 -*-
from odoo import api, fields, models


class GruposClientes(models.Model):
    _name = 'ops4g_fukuoka.grupos'
    _order = 'name'

    name = fields.Char(
        string="Nombre del grupo",
        required=True,
        help="Nombre del grupo",
    )

    color = fields.Char(
        string="Color del grupo",
    )

    _sql_constraints = [
        (
        	'name_uniq',
        	'UNIQUE (name)',
        	'¡¡Ya existe un grupo con este nombre!!'
        )
    ]
