# -*- coding: utf-8 -*-

"""The app module, containing the app factory function."""
from flask import Flask
from oneapi import user
from oneapi import nginx
from oneapi import commands


def create_app(config=None):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)

    register_blueprints(app)
    register_commands(app)
    return app


def register_blueprints(app):
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(nginx.views.blueprint)


def register_commands(app):
    app.cli.add_command(commands.test)

