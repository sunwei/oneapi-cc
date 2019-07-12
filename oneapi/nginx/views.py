# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, request

blueprint = Blueprint('nginx', __name__)


@blueprint.route('/api/nginx', methods=('GET',))
def nginx_conf_generator():
    return "my nginx configuration in generating..."

