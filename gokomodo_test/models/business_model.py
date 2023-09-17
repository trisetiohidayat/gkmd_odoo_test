# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GokomodoBusinessModel(models.Model):
    _name = 'gokomodo.business.model'
    _description = 'Gokomodo Business Model'

    name = fields.Char('Name',required=True)
    short_name = fields.Char('Short Name',required=True)