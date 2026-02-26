{
    'name': 'Gestión de Biblioteca',
    'version': '1.0',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'library_management/static/src/css/image_styles.css',
        ],
    },
}