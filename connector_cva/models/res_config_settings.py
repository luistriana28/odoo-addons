from odoo import models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.model
    def action_res_config_settings(self):
        res = self.create({'group_stock_multiple_locations': 1})
        res.execute()
        return True
