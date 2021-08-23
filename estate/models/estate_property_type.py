# Copyright 2021, Ventacero
# License LGPL-3.0 or later (http:.gnu.org/licenses/lgpt.html)

from odoo import api ,fields, models
# se importa fields desde la carpeta odoo fields.py y models.py


class EstatePropertyType(models.Model):
    _name = "estate.property.type"    # nombre tecnico
    _description = "Real Estate Property Type"  # nombre FUncional o Comun
    _order="sequence"
    name = fields.Char(
        required= True,
    )
    property_ids = fields.One2many(
        comodel_name = 'estate.property',
        inverse_name= "property_type_id",
        string ="Properties",
    )

    sequence = fields.Integer(
        default = 10
    )
    offers_ids = fields.One2many(
       comodel_name = 'estate.property.offer',
       inverse_name = 'property_type_id'
    )
    offer_count  = fields.Integer(
        compute="_compute_offer_count",
    )
    _sql_constraints = [
        ('name_uniq','unique(name)','El nombre ya existe'),
    ]
    @api.depends("offers_ids")
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offers_ids)