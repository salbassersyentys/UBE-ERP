# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_external_salesperson = fields.Boolean(string="Is external salesperson", default=False)
    """Whether this contact is an external salesperson"""
