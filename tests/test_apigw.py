# -*- coding: utf-8 -*-
"""Test ApiGW"""
import pytest
from domain.apigw.apigw import create_api_gw


@pytest.mark.usefixtures("api_gw_json_data")
def test_create_api_gw_by_json(api_gw_json_data):
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)

    assert api_gw_instance is not None
