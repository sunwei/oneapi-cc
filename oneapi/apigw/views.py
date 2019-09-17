# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint
from .serializers import (api_schema)
from .models import Api
from flask_apispec import marshal_with, use_kwargs
from flask_jwt_extended import current_user, jwt_required
from ddd_api_gateway import (create_api_gw, ApiGWBaseException)
from oneapi.exceptions import InvalidUsage
from oneapi.utils import (
    get_dict_from_base64_data,
    generate_nginx_conf,
    new_file_github
)
from oneapi.namespace.models import Namespace

blueprint = Blueprint('apigw', __name__)


@blueprint.route('/apigws', methods=('POST',))
@jwt_required
@use_kwargs(api_schema)
@marshal_with(api_schema)
def create_api(body, **kwargs):
    dict_body = get_dict_from_base64_data(body)
    if dict_body is None:
        raise InvalidUsage.unrecognized_file_format()
    try:
        api_gw = create_api_gw('json', dict_body)
    except ApiGWBaseException as e:
        raise InvalidUsage(str(e), status_code=422)

    namespace = Namespace.query.filter_by(name=api_gw.namespace).first()
    if not namespace:
        namespace = Namespace(current_user, api_gw.namespace, **kwargs)
        namespace.save()
        new_file_github(api_gw.namespace+'.conf')
    elif namespace.user != current_user:
        raise InvalidUsage.namespace_already_registered()

    a_api = Api(
        user=current_user,
        namespace=namespace,
        body=body,
        repository=api_gw.metadata.repository,
        description=api_gw.metadata.description,
        **kwargs
    )
    a_api.save()

    generate_nginx_conf(api_gw=api_gw)

    return a_api
