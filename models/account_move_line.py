# -*- coding: utf-8 -*-
# Copyright 2019 Appalach SPRL - Belgium
# (<http://www.appalach.be>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, exceptions


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    active = fields.Boolean("Actif")
