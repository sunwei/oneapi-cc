# -*- coding: utf-8 -*-
"""Domain Driven Design framework."""
from ..ddd import Aggregate


class Consumer(Aggregate):

    def check_mailbox(self):
        pass

