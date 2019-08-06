# -*- coding: utf-8 -*-

"""The app module, containing the app factory function."""
from flask import Flask
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from oneapi import user
from oneapi.user.views import get_user
from oneapi.nginx.views import nginx_conf_generator
from oneapi import nginx
from oneapi import commands


def create_app(config=None):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)

    register_blueprints(app)
    register_docs(app)
    register_commands(app)
    return app


def register_blueprints(app):
    app.register_blueprint(user.views.blueprint, url_prefix="/v1")
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(nginx.views.blueprint)


def register_docs(app):
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='RESTful API for oneapi.cc backend',
            version='v1',
            openapi_version="3.0.0",
            plugins=[MarshmallowPlugin()],
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
    })
    docs = FlaskApiSpec(app)
    docs.register(get_user, endpoint="get_user", blueprint="user")
    docs.register(nginx_conf_generator, endpoint="nginx_conf_generator", blueprint="nginx")


def register_commands(app):
    app.cli.add_command(commands.test)

