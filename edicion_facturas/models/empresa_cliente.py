# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Empresa_cliente(models.Model):
	_inherit = 'account.invoice'

	empresa_relacionada = fields.Char(
		string="Empresa del cliente",
		compute='obtener_empresa_cliente',
		store=True,
	)

	@api.multi
	@api.depends('partner_id')
	def obtener_empresa_cliente(self):
		for factura in self:
			id_cliente = factura.partner_id
			print ("*****************ID del cliente" + " " +str(id_cliente))
			id_empresa = id_cliente.parent_id
			print ("*****************ID de la empresa" + " " +str(id_empresa))
			nombre_empresa = id_empresa.name
			print ("Nombre de la empresa *******************" + " " + str(nombre_empresa))
			if nombre_empresa:
				factura.empresa_relacionada = str(nombre_empresa)
			else:
				factura.empresa_relacionada = ""

