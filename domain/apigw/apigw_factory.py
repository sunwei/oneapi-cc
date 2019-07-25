# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
import yaml
from .apigw import ApiGW
from .metadata import Metadata
from .api import Api
from .route_specification import RouteSpecification
from .apigw_validator import create_api_gw_validator
from ..exception.metadata_error import ApiGWMetadataError
from ..exception.api_error import ApiGWApiError
from ..exception.route_specification_error import ApiGWRouteSpecificationError


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
        for api in self.json_source["apis"]:
            if self.validator.check_api(api) is False:
                raise ApiGWApiError
        self.apis = self.json_source["apis"]
        return self

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

    def _init_apis(self, api_gw):
        for idx, val in enumerate(self.apis):
            if 0 == idx:
                api_gw.apis.append(Api(
                    name=val["name"],
                    path=val["path"],
                    specs=val["specs"]
                ))
            else:
                template_api = api_gw.apis[0]
                another_api = template_api.clone(
                    name=val["name"],
                    path=val["path"],
                    specs=val["specs"]
                )
                api_gw.apis.append(another_api)

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
        self._init_apis(api_gw)


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
        .with_apis()\
        .with_route_specification()\
        .build()

    return api_gw
