# -*- coding: utf-8 -*-
"""Test data"""
import os
import pytest
import json

TEST_PATH = os.path.abspath(os.path.dirname(__file__))
TEST_DATA_PATH = os.path.join(TEST_PATH, 'test_data')


@pytest.fixture(name='api_gw_json_data')
def api_gw_json_data():
    api_conf_json_path = os.path.join(TEST_DATA_PATH, 'api-conf-example.json')
    with open(api_conf_json_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data


@pytest.fixture(name='api_gw_wrong_json_data')
def api_gw_wrong_json_data():
    api_conf_json_path = os.path.join(TEST_DATA_PATH, 'api-conf-example-wrong.json')
    with open(api_conf_json_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data


@pytest.fixture(name='api_gw_wrong_route_specification_json_data')
def api_gw_wrong_route_specification_json_data():
    api_conf_json_path = os.path.join(TEST_DATA_PATH, 'api-conf-example-wrong-route-specification.json')
    with open(api_conf_json_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data
