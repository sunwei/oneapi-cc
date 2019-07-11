# -*- coding: utf-8 -*-
"""Domain Driven Design framework - Events."""
from collections import Collection
from typing import List, Iterator
from .event import Event


class Events(Collection):

    def __init__(self):
        self._events: List[Event] = []

    def __contains__(self, event: Event) -> bool:
        return event in self._events

    def __iter__(self) -> Iterator[Event]:
        yield from self._events

    def __len__(self) -> int:
        return len(self._events)

    def register(self, event: Event):
        self._events.append(event)

    def clear(self):
        self._events.clear()

