from odoo import models, fields

class Database(models.Model):
    _name = 'database.model'
    _description = 'Database Model'

    database_id = fields.Char(string='Database ID', required=True)
    server_id = fields.Many2one('server.model', string='Server', ondelete='cascade')
    database_name = fields.Char(string='Database Name', required=True)
    servertag_ids = fields.One2many('servertag.model', 'database_id', string='Server Tags')

    # Optional: Add created_at and updated_at
    # created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    # updated_at = fields.Datetime(string='Updated At', default=fields.Datetime.now)
