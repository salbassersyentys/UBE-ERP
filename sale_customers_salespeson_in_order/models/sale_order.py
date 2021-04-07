# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    user_id = fields.Many2one(default=lambda self: self.partner_id.user_id)
    """Updated to set customer's salesperson by default"""
