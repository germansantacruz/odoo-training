from odoo import fields, models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro de Biblioteca'

    name = fields.Char(string='Título', required=True)    