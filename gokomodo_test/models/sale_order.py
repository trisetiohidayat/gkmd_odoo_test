# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Customize Sale Order'

    business_model_id = fields.Many2one("gokomodo.business.model", required=True)
    
    def name_get(self):
        res = []
        for order in self:
            name = f"[{self.business_model_id.short_name}]" + " - " + order.name
            res.append((order.id, name))
        return res

    @api.onchange('business_model_id')
    def onchange_business_model_id(self):
        notif = False
        for rec in self:
            for order in rec.order_line:
                if order.tax_id:
                    notif = True
                order.tax_id = None
        
        if notif:
            return {'value':{},'warning':{'title':'Notification','message':'All tax removed because of change to business model'}}


        