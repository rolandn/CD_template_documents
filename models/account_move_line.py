
# -*- coding: utf-8 -*-
# © 2017 Eficent Business and IT Consulting Services S.L. (www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

#    active = fields.Boolean(string="Actif", default=True)
