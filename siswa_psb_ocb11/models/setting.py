from odoo import models, fields, api, _


class SiswaSetting(models.Model):
    _inherit = 'siswa.setting'

    default_psb_income_account = fields.Many2one('account.account', string="Income Account")
    default_psb_income_journal = fields.Many2one('account.journal', string="Income Journal")
