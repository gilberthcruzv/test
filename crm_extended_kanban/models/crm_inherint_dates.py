# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Crmleads(models.Model):
    _inherit = 'crm.lead'
    _order = "name, asc" 