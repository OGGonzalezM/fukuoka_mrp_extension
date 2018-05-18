# -*- coding: utf-8 -*-
from odoo import api, fields, models


class GruposClientes(models.Model):
    _name = 'ops4g_fukuoka.grupos'

    name = fields.Char(
        string="Nombre del grupo",
        required=True,
        index=True,
        help="Nombre del grupo"
    )

    color = fields.Char(
        string="Color del grupo",
        required=True
    )