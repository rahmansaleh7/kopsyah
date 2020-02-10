# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Amanah(models.Model):
    _name = 'kopsyah.amanah'

    name = fields.Char(string="No")
    parent_id = fields.Many2one(string="ID Anggota", comodel_name="res.partner")
    description = fields.Char(string="Deskripsi")