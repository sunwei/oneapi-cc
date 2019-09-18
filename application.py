# -*- coding: utf-8 -*-
"""Create an application instance, and this is the main entry for whole application."""

import os
from flask.helpers import get_debug_flag
from dotenv import load_dotenv
from oneapi.app import create_app
from oneapi.settings import DevConfig, StgConfig, ProdConfig

load_dotenv() if get_debug_flag() else print("prod: preload env from system environment")

ENV_CONF = DevConfig

oneapi_env = os.environ.get('ONEAPI_ENV', 'dev')
if oneapi_env == 'stg':
    ENV_CONF = StgConfig
elif oneapi_env == 'prod':
    ENV_CONF = ProdConfig

app = create_app(ENV_CONF)
