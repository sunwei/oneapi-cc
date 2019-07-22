# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
from ..ddd import ValueObject


class Metadata(ValueObject):

    def __init__(self, data):
        super().__init__()
        self.name = data["name"]
        self.author = data["author"]
        self.email = data["email"]
        self.repository = data["repository"]
        self.description = data["description"]
        self.annotations = data["annotations"]
