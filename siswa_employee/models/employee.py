# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _inherit = "hr.employee"

    street = fields.Char('Street')
    street2 = fields.Char('Street 2...')
    city = fields.Char('City')
    state_id = fields.Many2one('res.country.state', string="State")
    zip = fields.Char('ZIP')

    @api.onchange('job_id')
    def _onchange_job_id(self):
        # auto set department
        self.department_id = self.job_id.department_id.id
