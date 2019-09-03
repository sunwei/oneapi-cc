from marshmallow import Schema, fields, pre_load, post_dump
from oneapi.user.serializers import UserSchema


class ApiSchema(Schema):
    createdAt = fields.DateTime()
    updatedAt = fields.DateTime(dump_only=True)
    user = fields.Nested(UserSchema)
    id = fields.Int()
    body = fields.Str()

    # for the envelope
    api = fields.Nested('self', exclude=('api',), default=True, load_only=True)

    @pre_load
    def make_api(self, data):
        return data['api']

    @post_dump
    def dump_api(self, data):
        user = data['user']['user']
        data['owner'] = user['username']
        del data['user']
        return data

    class Meta:
        strict = True


api_schema = ApiSchema()
api_schemas = ApiSchema(many=True)
