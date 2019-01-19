# -*- coding: utf-8 -*-
{
    'name': "Siswa Kurikulum",

    'summary': """
        Rencana Pelaksanaan Pembelajaran""",

    'description': """
        Rencana Pelaksanaan Pembelajaran
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'siswa_ocb11', 'siswa_employee'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/kompetensi_inti_view.xml',
        'views/kompetensi_dasar_view.xml',
        'views/kategori_muatan_view.xml',
        'views/muatan_materi_view.xml',
        'views/rppm_setting_view.xml',
        'views/rppm_view.xml',
        'views/menu.xml',
        'reports/rppm_report_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
