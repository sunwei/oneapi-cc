# -*- coding: utf-8 -*-
"""Test ApiGW"""
from domain.apigw.route_specification import RouteSpecification

_test_route_specification = {
    "apiRef": "Warehouse Inventory",
    "upstreamRef": "Inventory",
    "policies":{
        "authentication": {
            "type": "Basic"
        }
    }
}


def test_create_route_specification():
    a_route_specification = RouteSpecification(
        api_ref=_test_route_specification["apiRef"],
        upstream_ref=_test_route_specification["upstreamRef"],
        policies=_test_route_specification["policies"])

    assert a_route_specification.api_ref is _test_route_specification["apiRef"]
    assert a_route_specification.upstream_ref is _test_route_specification["upstreamRef"]
    assert a_route_specification.policies is _test_route_specification["policies"]


def test_compare_route_specification():
    a_route_specification = RouteSpecification(
        api_ref=_test_route_specification["apiRef"],
        upstream_ref=_test_route_specification["upstreamRef"],
        policies=_test_route_specification["policies"])

    b_route_specification = RouteSpecification(
        api_ref=_test_route_specification["apiRef"],
        upstream_ref=_test_route_specification["upstreamRef"],
        policies=_test_route_specification["policies"])

    assert a_route_specification.same_as(b_route_specification) is True



