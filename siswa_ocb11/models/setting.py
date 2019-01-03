from odoo import models, fields, api, _


class SiswaSetting(models.Model):
    _name = 'siswa.setting'

    name = fields.Char('name', default=lambda self: self.env.user.company_id.name)
    default_siswa_number = fields.Selection(
        [('nis', 'NIS'), ('induk', 'Nomor System')], string="Default Siswa ID", default="induk")
    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.user.company_id.id, ondelete="cascade")

    def execute(self):
        # get setting on current company
        aSetting = self.env['siswa.setting'].search(
            [('company_id', '=', self.env.user.company_id.id)])
        if aSetting:
            aSetting.default_siswa_number = self.default_siswa_number
        # else:
        #     # create new setting for new company
        #     newSetting = self.env['siswa.setting'].create({
        #         'default_siswa_number': self.default_siswa_number
        #     })
        
        # self.write({
        #         'default_siswa_number' : self.default_siswa_number
        #     })
