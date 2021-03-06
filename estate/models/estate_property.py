# Copyright 2021, Ventacero
# License LGPL-3.0 or later (http:.gnu.org/licenses/lgpt.html)

from odoo import fields, models, api
from odoo.exceptions import ValidationError,UserError
from odoo.tools.float_utils import float_compare 
# se importa fields desde la carpeta odoo fields.py y models.py


class EstateProperty(models.Model):
    _name = "estate.property"    # nombre tecnico
    _description = "Properties"  # nombre FUncional o Comun
    _order ="id asc"
    name = fields.Char(
        string="Nombre", 
        required=True,
        default="Unknown",
        copy=False,
    )  
    # definir variable name con nombre por default
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False,
        default=lambda self: fields.Date.add(
            fields.Date.today(), months=+3) 
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(
        readonly=True,
        copy=False,
    )
    bedrooms = fields.Integer()
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
    active = fields.Boolean(
        default=True,
    )
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Offer Sold'),
            ('canceled', 'Canceled'),
        ],
        default='new',
        copy=False,
    ) 
    property_type_id = fields.Many2one(
        comodel_name = 'estate.property.type',
        ondelte = "restrict"
    )      
    buyer_id = fields.Many2one(
      comodel_name = "res.partner",
      copy = False,
      string="Buyer"
    )
    seller_id = fields.Many2one(
        comodel_name = "res.users",
        default = lambda self : self.env.user,
        string = "salesman",
    )
    tags_id=fields.Many2many(
        comodel_name = "estate.property.tag",
        string='Tags',
    )
    offers_ids = fields.One2many(
        comodel_name = "estate.property.offer",
        inverse_name = "property_id"
    )
    total_area = fields.Float(
        compute ="_compute_total_area",   
        inverse = "_inverse_total_area",
    )
    best_price = fields.Float(
        compute = "_compute_best_price",
    )
    date_deadline =  fields.Date(
        compute = "_compute_date_deadline",
        inverse = "_inverse_date_deadline",
    )
    validity = fields.Integer(
        default = 7,
    ) 
    _sql_constraints = [
        ('name_uniq','unique(name)','El nombre ya existe'),
        ('expected_price_positive','check(expected_price > 0)','El precio debde ser positivo'),
        ('selling_price_positve','check(selling_price > 0)','El precio de venta debe ser mayor a 0')
    ]




    # @api.model_create_multi
    # def create (self,vals_list):
    #     for var in vals_list
    #     return super().create(vals_list)

    @api.constrains('selling_price','expected_price')
    def _check_selling_price(self):
        for rec in self:
            expected_price = rec.expected_price *0.9
            if  rec.selling_price>0:  
                if float_compare(rec.selling_price,expected_price,2) == -1:
                    raise UserError("El precio de venta debe ser al menos el 90%"
                                "de el precio esperado"
                )    
    def action_sold(self):
        for rec in self:
            if rec.state == 'canceled':
                raise UserError('No se puede vender una propiedad cancelada')
            rec.state = 'sold'

    def action_canceled(self):
        for rec in self:
            if rec.state == 'sold':
                raise UserError("No se puede cancelar una propiedad vendida")
            rec.state ="canceled"

    @api.depends("validity","create_date")
    def _compute_date_deadline(self):
        for rec in self:
            create_date = rec.create_date or fields.Date.context_today(rec)
            rec.date_deadline = fields.Date.add(
                create_date, days=+rec.validity) 
    def _inverse_date_deadline(self):
        for rec in self:
            rec.validity = (rec.date_deadline - rec.create_date.date()).days

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area
    def _inverse_total_area(self):
        for rec in self:
            rec.garden_area = rec.total_area - rec.living_area
    
            
    @api.depends('offers_ids.price')
    def _compute_best_price(self):
        for rec in self:
            best_price =0
            if rec.offers_ids:
                best_price = max(rec.offers_ids.mapped('price'))
            rec.best_price = best_price
    def unlink(self):
        """ Delete all record(s) from table heaving record id in ids
        return True on success, False otherwise
    
        :return: True on success, False otherwise
        :rtype: Boolean
        """
        for rec in self:
            if rec.state not in ['new','canceled']:
                raise UserError('No puedes eliminar un registro que no sea nuevo o cancelado')
        return super().unlink()


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = 'price desc'
    price = fields.Float()
    status = fields.Selection(
        selection=[
            ('accepted','Accepted'),
            ("refused","Refused"),
        ],
        copy = False,
    )
    partner_id = fields.Many2one(
        comodel_name = "res.partner",
        required = True,
    )
    property_id = fields.Many2one(
        comodel_name = "estate.property",
        required = True,
        ondelete= 'cascade'
    )
    property_type_id = fields.Many2one(
        related = "property_id.property_type_id",
    )
    @api.model
    def create(self, vals):
        estate_property = self.env['estate.property'].browse(vals.get('property_id',False))
        prices = estate_property.offers_ids.mapped('price')
        if prices:
            max_offer = max(prices)
            if vals.get('price') < max_offer:
                raise UserError('No se puede aceptar una oferta menor a las existentes')
        return super().create(vals)
    def action_accept (self):
        for rec in self:
            if any ([x == 'accepted' for x in rec.property_id.offers_ids.mapped('status')]):
                raise UserError("Solo puedes aceptar una oferta.")
            rec.property_id.write({
                'buyer_id': rec.partner_id.id,
                'selling_price':rec.price,
            })
            rec.status = "accepted"
    def action_refuse(self):
        for rec in self:
            rec.status = "refused"
            
