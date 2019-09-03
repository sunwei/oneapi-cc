# -*- coding: utf-8 -*-
"""Application configuration settings for different environment"""
import os
from datetime import timedelta


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

    GITHUB_TOKEN = '5dbb8f1330c34480c66e05b732d62cb8cbdf1049'
    GITHUB_REPO = 'sunwei/nginx-apigw'
    GITHUB_REPO_BRANCH = 'master'


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL',
                                             'postgresql://localhost/example')
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '5dbb8f1330c34480c66e05b732d62cb8cbdf1049')
    GITHUB_REPO = os.environ.get('GITHUB_REPO', 'sunwei/nginx-apigw')
    GITHUB_REPO_BRANCH = os.environ.get('GITHUB_REPO_BRANCH', 'master')


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
