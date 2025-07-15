# -*- encoding: utf-8 -*-
{
    'name': 'IMPORTADOR DE SALDOS INICIALES C/S LOTES',
    'version': '1.0',
    'description': 'Agrega los campos y opciones de importación de saldos iniciales en el albaran. ESTE MODULO NO MODIFICA LA LOGICA DEL MODULO import_nro_lotes SOLO PERMITE SUBIR ARCHIVOS .xlsx',
    'author': 'ITGRUPO, Jhorel Revilla',
    'license': 'LGPL-3',
    'depends': [
        'stock',
        'kardex_fields_it'
    ],
    'data': [
        'security/res_groups.xml',
        'data/ir_attachment.xml',
        'views/stock_picking.xml',
    ],
    'auto_install': False,
    'application': False
}