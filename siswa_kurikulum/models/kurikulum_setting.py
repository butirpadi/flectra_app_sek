# -*- coding: utf-8 -*-

from odoo import models, fields, api
from pprint import pprint


class KurikulumSetting(models.Model):
    _name = 'kurikulum.setting'

    name = fields.Char('Name', default="General Setting")
    is_two_step_approval = fields.Boolean('Two level approval', default=False)
    first_approval_id = fields.Many2one('hr.employee', string="First Approval")
    first_job_id = fields.Many2one('hr.job', string="Job Position", related="first_approval_id.job_id")
    second_approval_id = fields.Many2one('hr.employee', string="Second Approval")
    second_job_id = fields.Many2one('hr.job', string="Job Position", related="second_approval_id.job_id")
