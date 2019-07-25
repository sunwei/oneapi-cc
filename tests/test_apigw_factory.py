# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from domain.apigw.apigw import ApiGW
from domain.apigw.metadata import Metadata
from domain.apigw.api import Api
from domain.apigw.route_specification import RouteSpecification
from domain.apigw.apigw_factory import create_api_gw
from domain.exception.metadata_error import ApiGWMetadataError
from domain.exception.api_error import ApiGWApiError
from domain.exception.route_specification_error import ApiGWRouteSpecificationError


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

    assert api_gw_instance.namespace == "warehouse"


@pytest.mark.usefixtures("api_gw_json_data")
def test_api_gw_with_metadata(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)

    assert type(api_gw_instance.metadata) is Metadata


@pytest.mark.usefixtures("api_gw_wrong_json_data")
def test_api_gw_with_metadata(api_gw_wrong_json_data):
    with pytest.raises(ApiGWMetadataError):
        assert create_api_gw("json", data=api_gw_wrong_json_data)


@pytest.mark.usefixtures("api_gw_json_data")
def test_api_gw_with_apis(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)

    assert api_gw_instance.apis is not None
    assert type(api_gw_instance.apis[0]) is Api
    assert type(api_gw_instance.apis[1]) is Api


@pytest.mark.usefixtures("api_gw_wrong_apis_json_data")
def test_api_gw_with_metadata(api_gw_wrong_apis_json_data):
    with pytest.raises(ApiGWApiError):
        assert create_api_gw("json", data=api_gw_wrong_apis_json_data)


# @pytest.mark.usefixtures("api_gw_json_data")
# def test_api_gw_with_route_specification(api_gw_json_data):
#     api_gw_instance = create_api_gw("json", data=api_gw_json_data)
#
#     assert type(api_gw_instance.route_specification) is RouteSpecification
#
#
# @pytest.mark.usefixtures("api_gw_wrong_route_specification_json_data")
# def test_api_gw_with_route_specification(api_gw_wrong_route_specification_json_data):
#     with pytest.raises(ApiGWRouteSpecificationError):
#         assert create_api_gw("json", data=api_gw_wrong_route_specification_json_data)


