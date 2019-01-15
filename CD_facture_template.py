# -*- coding: utf-8 -*-
# Copyright 2015 Agile Business Group sagl
# (<http://www.agilebg.com>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    duedate = fields.Date(string="Date limite de payement", required=False, track_visibility='onchange')