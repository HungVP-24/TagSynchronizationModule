from odoo import models, fields

class TagMapping(models.Model):
    _name = 'tagmapping.model'
    _description = 'Tag Mapping Model'

    server_tag_id = fields.Many2one('servertag.model', string='Server Tag', ondelete='cascade')
    local_tag_id = fields.Many2one('localtag.model', string='Local Tag', ondelete='cascade')

    # Optional: Add created_at and updated_at
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    updated_at = fields.Datetime(string='Updated At', default=fields.Datetime.now)
