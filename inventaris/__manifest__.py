# -*- coding: utf-8 -*-
{
    'name': "Inventaris Sekolah",

    'summary': """
        Aplikasi Inventaris Sekolah""",

    'description': """
        Aplikasi Inventaris Sekolah
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'default_setting_for_indonesian_app'],

    # always loaded
    'data': [
        'security/user_group.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_default_data.xml',
        'views/lokasi.xml',
        'views/brand.xml',
        'views/satuan.xml',
        'views/kategori.xml',
        'views/barang.xml',
        'views/color.xml',
        'views/vendor.xml',
        'views/sumber_dana.xml',
        'views/wizard_asset_move.xml',
        'views/wizard_scrap.xml',
        'views/setting.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
} 