# -*- coding: utf-8 -*-
"""Test ApiGW"""
from domain.apigw.api import Api


def test_create_api():
    api_test = Api("name", "path", "specs")

    assert api_test.name is "name"
    assert api_test.path is "path"
    assert api_test.specs is "specs"
    assert api_test.id is not None


def test_api_clone():
    api_test = Api("name", "path", "specs")
    clone_api = api_test.clone(name="anotherName", specs="anotherSpecs")

    assert clone_api.name is "anotherName"
    assert clone_api.path is "path"
    assert clone_api.specs is "anotherSpecs"
    assert clone_api.id is not api_test.id


