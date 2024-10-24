from odoo import models, fields

class ServerTag(models.Model):
    _name = 'servertag.model'
    _description = 'Server Tag Model'

    server_tag_id = fields.Char(string='Server Tag ID', required=True)
    database_id = fields.Many2one('database.model', string='Database', ondelete='cascade')
    tag_name = fields.Char(string='Tag Name', required=True)
    tag_mapping_ids = fields.One2many('tagmapping.model', 'server_tag_id', string='Tag Mappings')

    # Optional: Add created_at and updated_at
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    updated_at = fields.Datetime(string='Updated At', default=fields.Datetime.now)
