# Copyright 2021, Ventacero
# License LGPL-3.0 or later (http:.gnu.org/licenses/lgpt.html)

from odoo import fields, models
# se importa fields desde la carpeta odoo fields.py y models.py


class EstatePropertyType(models.Model):
    _name = "estate.property.type"    # nombre tecnico
    _description = "Real Estate Property Type"  # nombre FUncional o Comun
    _order="sequence"
    name = fields.Char(
        required= True,
    )
    property_ids = field_name_ids = fields.One2many(
        comodel_name = 'estate.property',
        inverse_name= "property_type_id",
        string ="Properties",
    )

    sequence = fields.Integer(
        default = 10
    )
    _sql_constraints = [
        ('name_uniq','unique(name)','El nombre ya existe'),
    ]