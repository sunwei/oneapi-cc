# -*- coding: utf-8 -*-
"""Application configuration settings for different environment"""
import os
from datetime import timedelta

LOG_REQUEST = 'ONEAPI.CC REQUEST %(asctime)s.%(msecs)03d ' \
              '%(filename)s:%(lineno)s request_id=%(request_id)s [%(levelname)s]: %(message)s'
LOG_STANDARD = 'ONEAPI.CC STANDARD %(asctime)s %(name)s %(levelname)s ''%(message)s [in %(pathname)s:%(lineno)d]'
LOG_SHORT = 'ONEAPI.CC SHORT %(asctime)s [%(levelname)s] %(name)s: %(message)s'

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {'format': LOG_STANDARD},
        'request': {'format': LOG_REQUEST},
        'short': {'format': LOG_SHORT},
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'request': {
            'level': 'DEBUG',
            'formatter': 'request',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'short': {
            'level': 'INFO',
            'formatter': 'short',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'request': {
            'handlers': ['request'],
            'level': 'DEBUG',
            'propagate': True
        },
        'werkzeug': {
            'handlers': ['short'],
            'level': 'INFO',
            'propagate': True
        },
    }
}


class SecretKey(object):
    SECRET_KEY = os.environ.get('ONEAPI_CC_SECRET', 'i-fell-not-good')


class AppDirectory(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class Config(SecretKey, AppDirectory):
    ENV = 'dev'
    DEBUG = True
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_HEADER_PREFIX = 'Token'
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:4100',
        'http://localhost:4100',
    ]
    JWT_HEADER_TYPE = 'Token'
    LOGGING = DEFAULT_LOGGING


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL',
                                             'postgresql://localhost/example')


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(10 ** 6)


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    BCRYPT_LOG_ROUNDS = 4
