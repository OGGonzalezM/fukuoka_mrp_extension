# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Empresa_cliente(models.Model):
	_inherit = 'account.invoice'

	empresa_relacionada = fields.Many2one(
		'res.partner',
		string="Empresa del cliente",
		related='partner_id',
		store=True,
	)

	
	grupo_cliente = fields.Many2one(
		'ops4g_fukuoka.grupos',
		string="Grupo del cliente",
		related='partner_id.x_fukuoka_grupo',
		store=True
	)

	color_grupo = fields.Char(
		string="Color del grupo",
		related='partner_id.x_fukuoka_grupo.color',
		store=True
	)
