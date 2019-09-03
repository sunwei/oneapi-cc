from flask import jsonify


def template(data, code=500):
    return {'message': {'errors': {'body': data}}, 'status_code': code}


USER_NOT_FOUND = template(['User not found'], code=404)
USER_ALREADY_REGISTERED = template(['User already registered'], code=409)
UNKNOWN_ERROR = template([], code=500)
ARTICLE_NOT_FOUND = template(['Article not found'], code=404)
COMMENT_NOT_OWNED = template(['Not your article'], code=422)

NAMESPACE_NOT_FOUND = template(['Namespace not found'], code=404)
NAMESPACE_ALREADY_REGISTERED = template(['Namespace already registered'], code=409)

UNRECOGNIZED_FILE_FORMAT = template(['Unrecognized file format! Only support yaml or json file now'], code=422)
APIGW_ERROR = template(['Api gateway error'], code=422)


class InvalidUsage(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = self.message
        return jsonify(rv)

    @classmethod
    def user_not_found(cls):
        return cls(**USER_NOT_FOUND)

    @classmethod
    def user_already_registered(cls):
        return cls(**USER_ALREADY_REGISTERED)

    @classmethod
    def unknown_error(cls):
        return cls(**UNKNOWN_ERROR)

    @classmethod
    def namespace_not_found(cls):
        return cls(**NAMESPACE_NOT_FOUND)

    @classmethod
    def namespace_already_registered(cls):
        return cls(**NAMESPACE_ALREADY_REGISTERED)

    @classmethod
    def unrecognized_file_format(cls):
        return cls(**UNRECOGNIZED_FILE_FORMAT)

    @classmethod
    def apigw_error(cls, e):
        return cls(**APIGW_ERROR)
