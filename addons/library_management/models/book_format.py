from odoo import fields, models

class LibraryBookFormat(models.Model):
    _name = 'library.book.format'
    _description = 'Formatos de Libro'
    
    name = fields.Char(string='Nombre del Formato', required=True)