# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
from ..ddd import Aggregate


class ApiGW(Aggregate):

    def __init__(self):
        super().__init__()
        self.version = None
        self.namespace = None
        self.metadata = None
        self.apis = []
        self.upstreams = []
        self.route_specifications = []

