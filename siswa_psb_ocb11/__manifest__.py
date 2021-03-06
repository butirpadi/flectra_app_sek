# -*- coding: utf-8 -*-
{
    'name': "PSB Siswa",

    'summary': """
        Aplikasi PSB Siswa""",

    'description': """
        Aplikasi PSB Siswa
        Untuk Sekolah PG/TK/RA
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'siswa_ocb11', 'siswa_keu_ocb11', 'siswa_tab_ocb11'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
         # 'data/ir_default_data.xml',
        'data/ir_default_biaya_registrasi_data.xml',
        'reports/report_formulir.xml',
        'reports/report_kwitansi_formulir.xml',
        'reports/report_kwitansi_registrasi.xml',
        'reports/report_calon_siswa.xml',
        'reports/report_distribusi_siswa.xml',
        'views/formulir.xml',
        'views/calon_siswa.xml',
        # 'views/wizard_distribusi_siswa_view.xml',
        'views/distribusi_siswa_view.xml',
        'views/wizard_report_calon_siswa_view.xml',
        'views/wizard_report_distribusi_siswa_view.xml',
        # 'views/biaya_registrasi.xml',
        'views/psb_setting_view.xml',
        'views/biaya_registrasi_manager_view.xml',
        'views/menu.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
} 