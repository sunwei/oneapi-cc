# -*- coding: utf-8 -*-
"""Domain Driven Design framework - Entity."""

import uuid


class Entity(object):

    def __init__(self, id_: uuid.UUID):
        super(Entity, self).__init__()
        self.id = id_

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return NotImplemented

        return self.id == other.id
