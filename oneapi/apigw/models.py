# coding: utf-8

from oneapi.database import (Model, db)


class Api(Model):

    __tablename__ = 'api'

    def __init__(self, yaml):
        self.yaml = yaml

    def __repr__(self):
        return "Api: " + self.yaml

    def save(self):
        pass

    def deploy(self):
        pass
