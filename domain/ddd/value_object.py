# -*- coding: utf-8 -*-
"""Domain Driven Design framework - Value Object."""
import copy
from dataclasses import dataclass


@dataclass
class ValueObject(object):

    def __eq__(self, other):
        if not isinstance(other, ValueObject):
            return NotImplemented

        return self.id == other.id

    def __copy__(self):
        return ValueObject(self.name)

    def __deepcopy__(self):
        return ValueObject(copy.deepcopy(self.name))
