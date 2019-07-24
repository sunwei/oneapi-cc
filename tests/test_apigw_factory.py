# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from domain.apigw.apigw import ApiGW
from domain.apigw.metadata import Metadata
from domain.apigw.route_specification import RouteSpecification
from domain.apigw.apigw_factory import create_api_gw
from domain.exception.ApiGWMetadataError import ApiGWMetadataError
from domain.exception.ApiGWRouteSpecificationError import ApiGWRouteSpecificationError


@pytest.mark.usefixtures("api_gw_json_data")
def test_create_api_gw_by_json(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)

    assert type(api_gw_instance) is ApiGW


@pytest.mark.usefixtures("api_gw_json_data")
def test_api_gw_with_version_1(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)

    assert api_gw_instance.version == "v1"


@pytest.mark.usefixtures("api_gw_json_data")
def test_api_gw_with_namespace(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)

    assert api_gw_instance.namespace == "default"


@pytest.mark.usefixtures("api_gw_json_data")
def test_api_gw_with_metadata(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)

    assert type(api_gw_instance.metadata) is Metadata


@pytest.mark.usefixtures("api_gw_wrong_json_data")
def test_api_gw_with_metadata(api_gw_wrong_json_data):
    with pytest.raises(ApiGWMetadataError):
        assert create_api_gw("json", data=api_gw_wrong_json_data)


@pytest.mark.usefixtures("api_gw_json_data")
def test_api_gw_with_route_specification(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)

    assert type(api_gw_instance.route_specification) is RouteSpecification


@pytest.mark.usefixtures("api_gw_wrong_route_specification_json_data")
def test_api_gw_with_route_specification(api_gw_wrong_route_specification_json_data):
    with pytest.raises(ApiGWRouteSpecificationError):
        assert create_api_gw("json", data=api_gw_wrong_route_specification_json_data)

