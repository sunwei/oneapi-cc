# -*- coding: utf-8 -*-
"""Test ApiGW validator"""
import pytest
from domain.apigw.apigw_validator import create_api_gw_validator


def test_create_validator_version_1():
    api_gw_validator_instance = create_api_gw_validator("v1")
    assert api_gw_validator_instance is not None


@pytest.mark.usefixtures("api_gw_json_data")
def test_v1_check_metadata_with_right_format(api_gw_json_data):
    api_gw_validator_instance = create_api_gw_validator("v1")
    result = api_gw_validator_instance.check_metadata(api_gw_json_data["metadata"])
    assert result is True


@pytest.mark.usefixtures("api_gw_json_data")
def test_v1_check_route_specification_with_right_format(api_gw_json_data):
    api_gw_validator_instance = create_api_gw_validator("v1")
    result = api_gw_validator_instance.check_route_specification(api_gw_json_data["routeSpecification"])
    assert result is True


@pytest.mark.usefixtures("api_gw_wrong_json_data")
def test_v1_check_metadata_with_wrong_format(api_gw_wrong_json_data):
    api_gw_validator_instance = create_api_gw_validator("v1")
    result = api_gw_validator_instance.check_metadata(api_gw_wrong_json_data["metadata"])
    assert result is False


@pytest.mark.usefixtures("api_gw_wrong_json_data")
def test_v1_check_route_specification_with_wrong_format(api_gw_wrong_json_data):
    api_gw_validator_instance = create_api_gw_validator("v1")
    result = api_gw_validator_instance.check_route_specification(api_gw_wrong_json_data["metadata"])
    assert result is False
