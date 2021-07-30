# Copyright 2021, Ventacero
# License LGPL-3.0 or later (http:.gnu.org/licenses/lgpt.html)

from odoo import fields, models
# se importa fields desde la carpeta odoo fields.py y models.py


class EstateProperty(models.Model):
    _name = "estate.property"    # nombre tecnico
    _description = "Properties"  # nombre FUncional o Comun

    name = fields.Char(
        string="Nombre", 
        required=True
    )  
    #definir variable name con nombre por default
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float( required=True)
    Selling_price = fields.Float()
    bedroms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ],
        # aqui se definen los nombres tecnicos y funcionales de la seleccion.
    )
