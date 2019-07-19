# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""


class ApiGWValidator(object):

    def check_metadata(self, metadata):
        raise NotImplementedError

    def check_route_specification(self, route_specification):
        raise NotImplementedError


class ApiGWValidatorV1(ApiGWValidator):
    def check_metadata(self, metadata):
        if metadata is None:
            return False
        return True

    def check_route_specification(self, route_specification):
        raise NotImplementedError


def create_api_gw_validator(version="v1"):
    """Factory"""
    api_gw_validator = {
        "v1": ApiGWValidatorV1
    }

    return api_gw_validator[version]()
