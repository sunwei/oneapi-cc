# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import yaml
import json
import base64
import requests
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


def push_to_github(filename, repo, branch, token):
    url = "https://api.github.com/repos/"+repo+"/contents/"+filename
    base64content = base64.b64encode(open(filename, "rb").read())

    data = requests.get(url+'?ref='+branch, headers={"Authorization": "token "+token}).json()
    sha = data['sha']

    if base64content.decode('utf-8')+"\n" != data['content']:
        message = json.dumps({
            "message": "update",
            "branch": branch,
            "content": base64content.decode("utf-8"),
            "sha": sha
        })
        resp = requests.put(
            url,
            data=message,
            headers={
                "Content-Type": "application/json",
                "Authorization": "token " + token
            }
        )
        return resp
    else:
        return False
