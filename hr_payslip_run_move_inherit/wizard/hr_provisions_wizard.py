# -*- coding:utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError
from datetime import *

class HrProvisionsWizard(models.TransientModel):
	_inherit = 'hr.provisions.wizard'

	def generate_move(self):
		Provision = self.env['hr.provisiones'].browse(self._context.get('active_id'))
		if Provision.asiento_contable:
			raise UserError('Borre el asiento actual para generar uno nuevo')
		MainParameter = self.env['hr.main.parameter'].get_main_parameter()
		if not MainParameter.provision_journal_id:
			raise UserError('No se ha configurado un Diario en el Menu Parametros Principales en la Pagina de Provisiones')
		if not MainParameter.type_doc_prov.id:
			raise UserError('No se ha configurado el tipo de comprobante para Provisiones')
		extra_line = {}
		if self.debit > self.credit:
			extra_line = {
						'account_id': self.account_id.id,
						'debit': 0,
						'credit': self.difference,
						'type_document_id' : MainParameter.type_doc_prov.id,
						'nro_comp' : 'PROVISION'+(Provision.payslip_run_id.name.code).replace("-", ""),
						'description': 'Ajuste por Redondeo',
						'partner_id':MainParameter.partner_id.id}
		if self.credit > self.debit:
			extra_line = {
						'account_id': self.account_id.id,
						'debit': self.difference,
						'credit': 0,
						'type_document_id' : MainParameter.type_doc_prov.id,
						'nro_comp' : 'PROVISION'+(Provision.payslip_run_id.name.code).replace("-", ""),
						'description': 'Ajuste por Redondeo',
						'partner_id':MainParameter.partner_id.id}
		move_lines = self._context.get('move_lines')
		if extra_line:
			move_lines.append(extra_line)
		# print("move_lines",move_lines)
		t = self.env['account.move'].create({
				'journal_id': MainParameter.provision_journal_id.id,
				'date': Provision.payslip_run_id.date_end,
				'glosa': 'PROVISION DE BBSS '+(Provision.payslip_run_id.name.code).replace("-", ""),
				'ref': 'PROVISION'+(Provision.payslip_run_id.name.code).replace("-", ""),
				'line_ids': [(0, 0, {
								'account_id': line['account_id'],
								'debit': line['debit'],
								'credit': line['credit'],
								'type_document_id' : MainParameter.type_doc_prov.id,
								'nro_comp' : 'PROVISION'+(Provision.payslip_run_id.name.code).replace("-", ""),
								'name': line['description'] if line['description'] else None,
								'partner_id': line['partner_id'] if line['partner_id'] is not None else MainParameter.partner_id.id,
								'analytic_account_id': line['analytic_account_id'] if 'analytic_account_id' in line else None,
								'analytic_tag_ids': ([(6,0, [line['analytic_tag_id']])]) if 'analytic_tag_id' in line and line['analytic_tag_id'] else None,
						} ) for line in move_lines
					]
			})
		t.action_post()
		Provision.asiento_contable = t.id
		return self.env['popup.it'].get_message('Asiento Generado')