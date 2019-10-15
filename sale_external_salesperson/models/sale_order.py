# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import formatLang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare



from werkzeug.urls import url_encode


class SaleOrder(models.Model):
    _inherit = "sale.order"

    user_id = fields.Many2one(
        #default=lambda self: self.env.user,
        domain=lambda self: ['|', ('groups_id', 'in', self.env.ref('sales_team.group_sale_salesman').id), ('partner_id.is_external_salesperson', '=', True)])
