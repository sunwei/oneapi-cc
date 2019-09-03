# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import yaml
import json
import base64
from oneapi.user.models import User  # noqa


def jwt_identity(payload):
    return User.get_by_id(payload)


def identity_loader(user):
    return user.id


def get_dict_from_base64_data(base64_encoded_data):
    decoded_data = base64.b64decode(base64_encoded_data)
    dict_data = yaml.safe_load(decoded_data)

    if isinstance(dict_data, dict):
        return dict_data
    else:
        return None
