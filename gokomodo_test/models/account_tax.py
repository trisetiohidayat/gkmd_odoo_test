# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountTax(models.Model):
    _inherit = 'account.tax'

    business_model_id = fields.Many2one(comodel_name="gokomodo.business.model")
