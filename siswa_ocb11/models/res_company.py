# -*- coding: utf-8 -*-
# Part of odoo. See LICENSE file for full copyright and licensing details.
import base64
import os
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError
from pprint import pprint

class Company(models.Model):
    _inherit = "res.company"

    @api.model
    def create(self, vals):
        result = super(Company, self).create(vals)
        # generate setting for new company        
        self.env['siswa.setting'].create({
            'name' : result.name,
            'company_id' : result.id,
        })

        # generate siswa_sequence
        self.env['ir.sequence'].create({
            'name' : 'Siswa Sequence ' + result.name,
            'code' : 'siswa.ocb11',
            'prefix' : '%(range_year)s',
            'padding' : '6',
            'company_id' : result.id,
        })

        return result


    @api.model
    def set_modoo_logo(self):
        print('--------------------------------')
        print('Set Modoo Logo')

        module_path = os.path.dirname(__file__).replace('models','')
        logo_path = os.path.join(module_path, 'static', 'src', 'img','logo_modoo.png')
        logo_os = open(logo_path, 'rb').read()
        logo_string = base64.b64encode(logo_os).decode('ascii')
        # self.env.cr.execute('UPDATE res_partner SET image=%s WHERE is_company=TRUE', (logo_string,))
        # size = (180, None)
        # self.env.cr.execute('UPDATE res_company SET logo_web=%s', (image_resize_image(img, size),))
        # mycomp = self.env['res.partner'].search([('is_company','=', True)])
        # print('----------------------------------')
        # print(logo_path)
        # print(mycomp[0].name)
        # print(mycomp[0].image)
        # print('----------------------------------')

        

