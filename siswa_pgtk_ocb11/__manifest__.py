# -*- coding: utf-8 -*-
{
    'name': "Siswa PG/TK",

    'summary': """
        Default data for Siswa Module for PG/TK""",

    'description': """
        Default data for Siswa Module for PG/TK
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'siswa_ocb11', 'siswa_keu_ocb11', 'siswa_tab_ocb11', 'siswa_psb_ocb11'],

    # always loaded
    'data': [
        'data/ir_model_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
} 