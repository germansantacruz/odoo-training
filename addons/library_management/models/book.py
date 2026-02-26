from odoo import fields, models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro de Biblioteca'

    def action_set_available(self):
        for record in self:
            record.state = 'available'

    name = fields.Char(string='Título', required=True)   
    isbn = fields.Char(string='ISBN')
    fecha_publicacion = fields.Date(string='Fecha de publicación') 
    descripcion = fields.Text(string='Descripción')
    price = fields.Float(string="Precio")
    # Campo de texto para la URL
    publisher_url = fields.Char(string='Web del Publicador',
        help="Sitio web oficial de la editorial o publicador.")
    # Campo especializado para imágenes
    # Definimos dimensiones máximas para optimizar el almacenamiento
    cover_image = fields.Image(
        string='Portada',
        max_width=1024,
        max_height=1024,
        verify_resolution=True
    )
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('available', 'Disponible'),
        ('borrowed', 'Prestado'),
        ('lost', 'Perdido/Dañado'),
    ], default='draft', string='Estado')
    active = fields.Boolean(string='Activo', default=True,
        help="Si está desmarcado, permite ocultar el libro sin eliminarlo de la base de datos.")
    
    # Relación One2many: Un libro -> Muchos ejemplares
    copy_ids = fields.One2many(
        'library.book.copy', 
        'book_id', 
        string='Ejemplares'
    )