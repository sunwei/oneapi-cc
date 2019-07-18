# -*- coding: utf-8 -*-
"""Test ApiGW"""
import os
import pytest
import json
from domain.apigw.apigw import create_api_gw

TEST_PATH = os.path.abspath(os.path.dirname(__file__))
TEST_DATA_PATH = os.path.join(TEST_PATH, 'test_data')


@pytest.fixture(name='api_gw_json_data')
def fixture_api_gw_json_data():
    api_conf_json_path = os.path.join(TEST_DATA_PATH, 'api-conf-example.json')
    print(api_conf_json_path)
    with open(api_conf_json_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data


def test_create_api_gw_by_json(api_gw_json_data):
    print("====")
    print(api_gw_json_data)
    api_gw_instance = create_api_gw("json", data=api_gw_json_data)
    if api_gw_instance is None:
        assert False

    assert True


