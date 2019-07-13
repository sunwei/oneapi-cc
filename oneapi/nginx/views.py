# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, jsonify
from .builder import start_build

blueprint = Blueprint('nginx', __name__)


@blueprint.route('/api/nginx', methods=('GET',))
def nginx_conf_generator():
    return jsonify(start_build())

