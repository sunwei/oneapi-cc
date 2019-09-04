from marshmallow import Schema, fields, pre_load, post_dump
from oneapi.user.serializers import UserSchema


class NamespaceSchema(Schema):
    createdAt = fields.DateTime()
    updatedAt = fields.DateTime(dump_only=True)
    user = fields.Nested(UserSchema)
    id = fields.Int()
    name = fields.Str()

    # for the envelope
    namespace = fields.Nested('self', exclude=('namespace',), default=True, load_only=True)

    @pre_load
    def make_namespace(self, data):
        return data['namespace']

    @post_dump
    def dump_namespace(self, data):
        return {'namespace': data}

    class Meta:
        strict = True


namespace_schema = NamespaceSchema()
namespace_schemas = NamespaceSchema(many=True)
