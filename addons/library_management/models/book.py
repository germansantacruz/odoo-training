from odoo import fields, models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro de Biblioteca'

    name = fields.Char(string='Título', required=True)   
    isbn = fields.Char(string='ISBN')
    fecha_publicacion = fields.Date(string='Fecha de publicación') 
    descripcion = fields.Text(string='Descripción')
    price = fields.Float(string="Precio")
    state = fields.Selection([
        ('available', 'Disponible'),
        ('borrowed', 'Prestado'),
    ], default='available', string='Estado')
    active = fields.Boolean(string='Activo', default=True,
        help="Si está desmarcado, permite ocultar el libro sin eliminarlo de la base de datos.")