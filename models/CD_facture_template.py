# -*- coding: utf-8 -*-
# Copyright 2019 Appalach SPRL - Belgium
# (<http://www.appalach.be>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, exceptions


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    duedate = fields.Date(string="Date limite de payement", required=False, track_visibility='onchange')
    message_id = fields.Many2one('message.invoice', string='Message', store=True, required=False, track_visibility='onchange', help="Remarque sur le taux de TVA appliqué. Ex : Autoliquidation de la TVA.")
    num_affaire = fields.Char(string="Numéro d'affaire", required=False, track_visibility='onchange')

    est_be = fields.Boolean(string="ISOC Belge", required=False, track_visibility='onchange', default=True)
    est_lux = fields.Boolean(string="ISOC Luxembourgeois", required=False, track_visibility='onchange', default=False)
    est_fr = fields.Boolean(string="ISOC Francais", required=False, track_visibility='onchange', default=False)

#    _sql_constraints = [('num_affaire_unique', 'unique(num_affaire)', 'Ce numéro d affaire existe déjà !')]

class Message(models.Model):
    _name = 'message.invoice'

    name = fields.Char(string="Text du message", required=True)
    active = fields.Boolean('Actif ?', default=True)

class invoice(models.Model):
    _inherit = 'account.invoice'

    @api.one
    def bouton_draft(self):
        self.write({
            'state': 'draft'
        })

class ResPartner(models.Model):
    _inherit = "res.partner"

    ref = fields.Char()
    _sql_constraints = [('ref_unique', 'unique(ref)', 'Cette référence existe déjà !')]
