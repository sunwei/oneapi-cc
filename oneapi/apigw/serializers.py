# coding: utf-8

from marshmallow import Schema, fields


class ApiSchema(Schema):
    yaml = fields.Str()


api_schema = ApiSchema()
