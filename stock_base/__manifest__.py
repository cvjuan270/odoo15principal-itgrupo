{
    'name': 'Personalizaciones de Inventario',
    'version': '1.0',
    'description': 'Personalizaciones de Inventario',
    'author': 'ITGRUPO, Jhorel Revilla',
    'license': 'LGPL-3',
    'depends': [
        'kardex_fisico_it'
    ],
    'data': [
        'reports/report_delivery_document.xml',
        'views/stock_picking.xml',
        'views/type_operation_kardex.xml',
    ],
    'auto_install': False,
    'application': False,
}