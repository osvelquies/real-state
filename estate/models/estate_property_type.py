# Copyright 2021, Ventacero
# License LGPL-3.0 or later (http:.gnu.org/licenses/lgpt.html)

from odoo import fields, models
# se importa fields desde la carpeta odoo fields.py y models.py


class EstatePropertyType(models.Model):
    _name = "estate.property.type"    # nombre tecnico
    _description = "Real Estate Property Type"  # nombre FUncional o Comun

    name = fields.Char(
        required= True,
    )