# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
import yaml
from ..ddd import Aggregate


class ApiGW(Aggregate):

    def check_mailbox(self):
        pass


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
        self.yaml_source = data
        self.version = None
        self.metadata = None
        self.route_specification = None

    def with_version(self):
        return self

    def with_metadata(self):
        return self

    def with_route_specification(self):
        return self

    def build(self):
        return self


def create_api_gw(formatter="yaml", data=None):
    """Factory"""
    api_gw_builder = {
        "yaml": lambda yaml_data: ApiGWJsonBuilder(yaml.safe_load(yaml_data)),
        "json": lambda json_data: ApiGWJsonBuilder(json_data)
    }

    builder = api_gw_builder[formatter](data)
    api_gw = builder.with_version().with_metadata().with_route_specification()

    return api_gw
