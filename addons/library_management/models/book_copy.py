from odoo import fields, models

class LibraryBookCopy(models.Model):
    _name = 'library.book.copy'
    _description = 'Ejemplar físico de un libro'

    name = fields.Char(string='Código de Barras', required=True)
    
    # Muchos ejemplares -> Un libro (Parent)
    book_id = fields.Many2one('library.book', string='Libro', ondelete='cascade')
    
    # Muchos ejemplares -> Un Formato (Entidad Catálogo)
    format_id = fields.Many2one('library.book.format', string='Formato', required=True)
    
    status = fields.Selection([
        ('good', 'Buen Estado'),
        ('worn', 'Desgastado'),
        ('damaged', 'Dañado')
    ], default='good', string='Estado Físico')