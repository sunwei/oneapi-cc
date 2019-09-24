# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import yaml
import json
import base64
import requests
from flask import current_app
from oneapi.user.models import User  # noqa

from ddd_nginx.nginx import Nginx
from ddd_nginx.server import Server
from ddd_nginx.location import Location, LocationRewrite, LocationProxy
from ddd_nginx.upstream import Upstream


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


def new_file_github(filename):
    url = "https://api.github.com/repos/"+current_app.config['GITHUB_REPO']+"/contents/nginx/api_gw.d/"+filename
    base64content = base64.b64encode('init content...'.encode('utf-8'))

    message = json.dumps({
        "message": "create",
        "branch": current_app.config['GITHUB_REPO_BRANCH'],
        "content": base64content.decode("utf-8")
    })
    resp = requests.put(
        url,
        data=message,
        headers={
            "Content-Type": "application/json",
            "Authorization": "token " + current_app.config['GITHUB_TOKEN']
        }
    )
    return resp


def push_to_github(filename):
    url = "https://api.github.com/repos/"+current_app.config['GITHUB_REPO']+"/contents/nginx/api_gw.d/"+filename
    base64content = base64.b64encode(open("./dumps_dir/all-in-one.conf", "rb").read())

    data = requests.get(url+'?ref='+current_app.config['GITHUB_REPO_BRANCH'],
                        headers={"Authorization": "token "+current_app.config['GITHUB_TOKEN']}).json()
    sha = data['sha']

    if base64content.decode('utf-8')+"\n" != data['content']:
        message = json.dumps({
            "message": "update",
            "branch": current_app.config['GITHUB_REPO_BRANCH'],
            "content": base64content.decode("utf-8"),
            "sha": sha
        })
        resp = requests.put(
            url,
            data=message,
            headers={
                "Content-Type": "application/json",
                "Authorization": "token " + current_app.config['GITHUB_TOKEN']
            }
        )
        return resp
    else:
        return False


def generate_nginx_conf(api_gw):
    nginx = Nginx(host="oneapi.cc")
    nginx.namespace = api_gw.namespace

    up_host = None
    for upstream in api_gw.upstreams:
        up_host = upstream.host
        up_str = Upstream(name=upstream.name)
        for endpoint in upstream.endpoints:
            up_str.append(endpoint)
        nginx.append(up_str)

    a_server = Server(name=nginx.namespace)
    a_server.set_var("$api_name", "-")
    a_server.disable_tls()
    nginx.append(a_server)

    internal_location = Location(
        name="/_{}".format(api_gw.namespace),
        internal=True,
    )
    internal_location.set_var("$api_name", "Warehouse")
    internal_location.append(LocationProxy(up_host))

    def get_api(api_ref):
        the_api = None
        for a_api in api_gw.apis:
            if a_api.name == api_ref:
                the_api = a_api
                break

        return the_api

    def get_upstream(upstream_ref):
        the_upstream = None
        for a_upstream in api_gw.upstreams:
            if a_upstream.name == upstream_ref:
                the_upstream = a_upstream
                break

        return the_upstream

    for route_spec in api_gw.route_specifications:
        api = get_api(route_spec.api_ref)
        upstream = get_upstream(route_spec.upstream_ref)
        a_location = Location(
            name=api.path,
            internal=False
        )
        a_location.set_var("$upstream", upstream.name)
        a_location.append(LocationRewrite(internal_location))
        nginx.append(a_location)

    nginx.append(internal_location)

    root_dir = "./dumps_dir"
    nginx.dumps(root_dir)
