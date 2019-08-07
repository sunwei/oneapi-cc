# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, jsonify
from .builder import start_build
from .serializers import (api_schema)
from flask_apispec import marshal_with, use_kwargs

blueprint = Blueprint('apigw', __name__)


@blueprint.route('/apigw/apis', methods=('POST',))
@use_kwargs(api_schema)
@marshal_with(api_schema)
def nginx_conf_generator(yaml):
    return jsonify(start_build())

