# -*- coding: utf-8 -*-
"""Test ApiGW"""
from domain.apigw.upstream import Upstream

_endpoints = [
    "api1.com",
    "api2.com",
    "api3.com"
]


def test_create_api():
    upstream_test = Upstream("name", _endpoints)

    assert upstream_test.name is "name"
    assert upstream_test.endpoints is _endpoints
    assert upstream_test.id is not None


def test_api_clone():
    upstream_test = Upstream("name", _endpoints)
    clone_api = upstream_test.clone(name="anotherName")

    assert clone_api.name is "anotherName"
    assert upstream_test.endpoints is _endpoints
    assert clone_api.id is not upstream_test.id


