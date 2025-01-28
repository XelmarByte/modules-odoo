# -*- coding: utf-8 -*-

from odoo import models, fields, api


class agenda(models.Model):
     _name = 'agenda.agenda'
     _description = 'agenda.agenda'

     Nombre = fields.Char()
     Telefono = fields.Char() 


