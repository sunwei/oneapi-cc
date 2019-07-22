# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
import yaml
from ..ddd import Aggregate


class ApiGW(Aggregate):

    def __init__(self):
        self.version = None
        self.namespace = None
        self.metadata = None
        self.route_specification = None

    def check_mailbox(self):
        pass
