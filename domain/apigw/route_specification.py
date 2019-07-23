# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
from ..ddd import ValueObject


class RouteSpecification(ValueObject):

    def __init__(self, data):
        super().__init__()
        self.routes = data


