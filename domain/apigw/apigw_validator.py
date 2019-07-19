# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""


class ApiGWValidator(object):

    def check_metadata(self, metadata):
        raise NotImplementedError

    def check_route_specification(self, route_specification):
        raise NotImplementedError


class ApiGWValidatorV1(ApiGWValidator):
    def check_metadata(self, metadata):
        check_result = False
        if metadata is not None:
            if 'name' in metadata \
                    and 'email' in metadata \
                    and 'description' in metadata \
                    and 'repository' in metadata:
                check_result = True
        return check_result

    def check_route_specification(self, route_specification):
        raise NotImplementedError


def create_api_gw_validator(version="v1"):
    """Factory"""
    api_gw_validator = {
        "v1": ApiGWValidatorV1
    }

    return api_gw_validator[version]()
