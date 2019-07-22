# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
import yaml
from .apigw import ApiGW


class ApiGWBuilder(object):
    def with_version(self):
        raise NotImplementedError

    def with_metadata(self):
        raise NotImplementedError

    def with_route_specification(self):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError


class ApiGWJsonBuilder(ApiGWBuilder):
    """Builder"""
    def __init__(self, data):
        self.json_source = data
        self.version = None
        self.namespace = None
        self.metadata = None
        self.route_specification = None
        self.validator = None

    def with_version(self):
        self.version = self.json_source["version"]
        return self

    def with_metadata(self):
        return self

    def with_route_specification(self):
        return self

    def build(self):
        api_gw = ApiGW()
        api_gw.version = self.version
        return api_gw


def create_api_gw(formatter="yaml", data=None):
    """Factory"""
    api_gw_builder = {
        "yaml": lambda yaml_data: ApiGWJsonBuilder(yaml.safe_load(yaml_data)),
        "json": lambda json_data: ApiGWJsonBuilder(json_data)
    }

    builder = api_gw_builder[formatter](data)
    api_gw = builder.with_version().with_metadata().with_route_specification().build()

    return api_gw
