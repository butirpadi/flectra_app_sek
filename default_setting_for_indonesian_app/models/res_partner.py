# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from pprint import pprint
from datetime import datetime, date


class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def set_default_domain_user(self):
        # get res_id
        action_obj = self.env['ir.model.data'].search([
            ('name','=','action_res_users')
            ])

        # update domain 
        self.env['ir.actions.act_window'].search([
            ('id', '=', action_obj[0].res_id)
        ]).write({
            'domain' : "[('login','!=','root')]",
            'context' : "{'search_default_no_share': 1, 'default_tz':'Asia/Jakarta'}",
        })

        # update timezone root user
        root_user = self.env['res.users'].search([
            ('login','=','root')
        ])

        self.env.cr.execute("update res_partner set tz = 'Asia/Jakarta' where id = " + str(root_user[0].partner_id.id))
    
