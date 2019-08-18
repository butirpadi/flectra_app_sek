from odoo import models, fields, api, exceptions, _
from odoo.addons import decimal_precision as dp
from datetime import datetime
from pprint import pprint


class AccountMove(models.Model):
    _inherit = "account.move"
