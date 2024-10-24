from odoo import models, fields

class Server(models.Model):
    _name = 'server.model'
    _description = 'Server Model'

    server_id = fields.Char(string='Server ID', required=True)
    domain = fields.Char(string='Domain', required=True)
    server_name = fields.Char(string='Server Name', required=True)
    database_ids = fields.One2many('database.model', 'server_id', string='Databases')

    # Optional: Add created_at and updated_at
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    updated_at = fields.Datetime(string='Updated At', default=fields.Datetime.now)
