# coding: utf-8

from flask import Blueprint
from flask_apispec import marshal_with, use_kwargs
from flask_jwt_extended import current_user, jwt_required, jwt_optional

from .serializers import namespace_schema
from oneapi.exceptions import InvalidUsage
from oneapi.namespace.models import Namespace

blueprint = Blueprint('namespaces', __name__)


@blueprint.route('/namespaces/<namespace>', methods=('GET',))
@jwt_optional
@marshal_with(namespace_schema)
def get_namespace(namespace):
    namespace = Namespace.query.filter_by(name=namespace).first()
    if not namespace:
        raise InvalidUsage.namespace_not_found()
    return namespace


@blueprint.route('/namespaces', methods=('POST',))
@jwt_required
@use_kwargs(namespace_schema)
@marshal_with(namespace_schema)
def register_namespace_for_user(name, **kwargs):
    the_namespace = Namespace.query.filter_by(name=name).first()
    if the_namespace:
        raise InvalidUsage.namespace_already_registered()
    a_namespace = Namespace(current_user, name, **kwargs)
    a_namespace.save()
    return a_namespace

