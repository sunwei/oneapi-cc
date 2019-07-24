# -*- coding: utf-8 -*-
"""Domain Driven Design framework - Value Object."""


class ValueObject(object):
    def same_as(self, other):
        return self == other

