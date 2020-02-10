# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Amanah(models.Model):
    _name = 'kopsyah.amanah'

    name = fields.Char(string="Nama")
    description = fields.Char(string="Deskripsi")