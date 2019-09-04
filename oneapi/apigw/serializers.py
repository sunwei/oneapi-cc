from marshmallow import Schema, fields, pre_load, post_dump
from oneapi.user.serializers import UserSchema
from oneapi.namespace.serializers import NamespaceSchema


class ApiSchema(Schema):
    createdAt = fields.DateTime()
    updatedAt = fields.DateTime(dump_only=True)
    user = fields.Nested(UserSchema)
    namespace = fields.Nested(NamespaceSchema)
    id = fields.Int()
    body = fields.Str()
    repository = fields.Str()
    description = fields.Str()

    # for the envelope
    api = fields.Nested('self', exclude=('api',), default=True, load_only=True)

    @pre_load
    def make_api(self, data):
        return data['api']

    @post_dump
    def dump_api(self, data):
        return {'api': data}

    class Meta:
        strict = True


api_schema = ApiSchema()
api_schemas = ApiSchema(many=True)
