# -*- coding: utf-8 -*-
"""Domain Driven Design framework - Aggregate Root."""

from .events import Events


class Aggregate(object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._events: Events = None

    @property
    def events(self) -> Events:
        if getattr(self, '_events', None) is None:
            self._events = Events()
        return self._events

    def clear_events(self):
        self._events.clear()
