# -*- coding: utf-8 -*-
{
    'name': "Siswa Letter",

    'summary': """
        Surat/Menyurat for Siswa """,

    'description': """
        Surat/Menyurat for Siswa 
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'siswa_ocb11', 'siswa_keu_ocb11', 'siswa_tab_ocb11'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/ir_default_data.xml',
        'views/wizard_surat_tagihan.xml',
        'views/surat.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application': True,
    'installabele': True
}
