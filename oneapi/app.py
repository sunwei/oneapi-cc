# -*- coding: utf-8 -*-

"""The app module, containing the app factory function."""
from flask import Flask
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from sqlalchemy import text
from healthcheck import HealthCheck, EnvironmentDump
from flask_logger_decorator import debug
from oneapi.extensions import bcrypt, cache, db, migrate, jwt, cors, logger
from oneapi import user, profile, namespace, apigw, commands
from oneapi.user.views import (register_user, login_user)
from oneapi.profile.views import (get_profile)
from oneapi.exceptions import InvalidUsage


def create_app(config=None):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config)

    register_shell_context(app)
    register_extensions(app)
    register_error_handlers(app)
    register_blueprints(app)
    register_docs(app)
    register_commands(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    health_check(app)
    logger.init_app(app)


def register_error_handlers(app):

    def error_handler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(InvalidUsage)(error_handler)


def register_shell_context(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': user.models.User,
            'UserProfile': profile.models.UserProfile,
        }

    app.shell_context_processor(shell_context)


def register_blueprints(app):
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(user.views.blueprint, origins=origins)
    cors.init_app(profile.views.blueprint, origins=origins)
    cors.init_app(namespace.views.blueprint, origins=origins)

    app.register_blueprint(user.views.blueprint, url_prefix="/api/v1")
    app.register_blueprint(user.views.blueprint, url_prefix="/api")
    app.register_blueprint(profile.views.blueprint, url_prefix="/api/v1")
    app.register_blueprint(profile.views.blueprint, url_prefix="/api")
    app.register_blueprint(namespace.views.blueprint, url_prefix="/api/v1")
    app.register_blueprint(namespace.views.blueprint, url_prefix="/api")
    app.register_blueprint(apigw.views.blueprint, url_prefix="/api/v1")
    app.register_blueprint(apigw.views.blueprint, url_prefix="/api")


def register_docs(app):
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='RESTful API for oneapi.cc backend',
            version='v1',
            openapi_version="2.0.0",
            plugins=[MarshmallowPlugin()],
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
    })
    docs = FlaskApiSpec(app)
    docs.register(register_user, endpoint="register_user", blueprint="user")
    docs.register(login_user, blueprint="user")
    docs.register(get_profile, blueprint="profiles")


def register_commands(app):
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)


def health_check(app):
    health = HealthCheck(app, "/healthcheck")
    # env_dump = EnvironmentDump(app, "/environment")

    def db_status():
        try:
            query_result = db.engine.execute(text("SELECT 1"))
            debug("oneapi-sql-logger", str(query_result))
            return True, "db connection ok"
        except Exception as e:
            debug("oneapi-sql-logger", str(e))
            return False, "db connection failed"

    health.add_check(db_status)

    # def application_data():
    #     return {"maintainer": "Wayde Sun",
    #             "git_repo": "https://github.com/sunwei/oneapi-cc"}

    # env_dump.add_section("application", application_data)
