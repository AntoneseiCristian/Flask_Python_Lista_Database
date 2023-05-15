from marshmallow import Schema, fields

class ProdusSchema(Schema):
    id = fields.Str(dump_only=True)
    nume = fields.Str(required=True)
    pret = fields.Float(required=True)
    magazin_id = fields.Str(required=True)

class ProdusSchema(Schema):
    nume = fields.Str(required=True)
    pret = fields.Float(required=True)

class MagazinSchema(Schema):
    id = fields.Str(dump_only=True)
    nume = fields.Str(required=True)