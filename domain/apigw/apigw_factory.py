# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
import yaml
from .apigw import ApiGW
from .metadata import Metadata
from .route_specification import RouteSpecification
from .apigw_validator import create_api_gw_validator
from ..exception.ApiGWMetadataError import ApiGWMetadataError
from ..exception.ApiGWRouteSpecificationError import ApiGWRouteSpecificationError


class ApiGWBuilder(object):
    def with_version(self):
        raise NotImplementedError

    def with_metadata(self):
        raise NotImplementedError

    def with_apis(self):
        raise NotImplementedError

    def with_upstreams(self):
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
        self.apis = None
        self.upstreams = None
        self.route_specification = None
        self.validator = None

    def _build_validator(self):
        self.validator = create_api_gw_validator(self.version)

    def with_version(self):
        self.version = self.json_source["version"]
        self._build_validator()
        return self

    def with_namespace(self):
        self.namespace = self.json_source["namespace"] or "default"
        return self

    def with_apis(self):
        raise NotImplementedError

    def with_upstreams(self):
        raise NotImplementedError

    def with_metadata(self):
        if self.validator.check_metadata(self.json_source["metadata"]) is True:
            self.metadata = self.json_source["metadata"]
        else:
            raise ApiGWMetadataError()

        return self

    def with_route_specification(self):
        for route_spec in self.json_source["routeSpecification"]:
            if self.validator.check_route_specification(route_spec) is False:
                raise ApiGWRouteSpecificationError()
        self.route_specification = self.json_source["routeSpecification"]

        return self

    def build(self):
        api_gw = ApiGW()
        api_gw.version = self.version
        api_gw.namespace = self.namespace
        api_gw.metadata = Metadata(
            author=self.metadata["author"],
            email=self.metadata["email"],
            repository=self.metadata["repository"],
            description=self.metadata["description"]
        )
        # api_gw.route_specification = RouteSpecification(self.route_specification)
        return api_gw


def create_api_gw(formatter="yaml", data=None):
    """Factory"""
    api_gw_builder = {
        "yaml": lambda yaml_data: ApiGWJsonBuilder(yaml.safe_load(yaml_data)),
        "json": lambda json_data: ApiGWJsonBuilder(json_data)
    }

    builder = api_gw_builder[formatter](data)
    api_gw = builder.with_version()\
        .with_namespace()\
        .with_metadata()\
        .with_route_specification()\
        .build()

    return api_gw
