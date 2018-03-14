# -*- coding: utf-8 -*-
from odoo import models, fields


class Edicionmrp(models.Model):
    _inherit = 'mrp.production'

    origin = fields.Many2one(
        'sale.order',
        string="Documento Origen",
    )
