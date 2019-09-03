# coding: utf-8
import datetime as dt
from oneapi.database import (Model, db, Column, reference_col, relationship)


class Api(Model):

    __tablename__ = 'api'
    id = db.Column(db.Integer, primary_key=True)
    body = Column(db.Text)
    createdAt = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updatedAt = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    user_id = reference_col('users', nullable=False)
    user = relationship('User', backref=db.backref('api'))

    def __init__(self, user, body, **kwargs):
        db.Model.__init__(self, user=user, body=body, **kwargs)
