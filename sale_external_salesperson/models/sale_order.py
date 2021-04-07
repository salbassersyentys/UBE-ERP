# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    user_id = fields.Many2one(
        domain=lambda self: ['|', ('groups_id', 'in', self.env.ref('sales_team.group_sale_salesman').id), ('partner_id.is_external_salesperson', '=', True)])
    """Updated to fetch partner marked as external salesperson"""
