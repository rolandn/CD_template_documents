# -*- coding: utf-8 -*-
# Copyright 2019 Appalach SPRL - Belgium
# (<http://www.appalach.be>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, exceptions

# Modification du res.partner pour y renseigner le taux d'escompte obtenu
class ResPartner(models.Model):
    _inherit = "res.partner"

    escompte = fields.Integer(string="Taux d escompte appliqué par le fournisseur",
                              required=False,
                              track_visibility='onchange')


# Modification du modèle facture
class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    escompte_id = fields.Integer("res.partner",
                                 related='partner_id.escompte',
                                 readonly=True,
                                 sting="Taux d escompte obtenu",
                                 required=False,
                                 track_visibility='onchange')
