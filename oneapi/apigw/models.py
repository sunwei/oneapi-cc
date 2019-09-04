# coding: utf-8
import datetime as dt
from oneapi.database import (Model, db, Column, reference_col, relationship)


class Api(Model):

    __tablename__ = 'api'
    id = db.Column(db.Integer, primary_key=True)
    body = Column(db.Text)
    repository = Column(db.String(200), nullable=True)
    description = Column(db.String(300), nullable=True)
    createdAt = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updatedAt = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    user_id = reference_col('users', nullable=False)
    user = relationship('User', backref=db.backref('api'))
    namespace_id = reference_col('namespace', nullable=False)
    namespace = relationship('Namespace', backref=db.backref('api'))

    def __init__(self, user, namespace, body, repository, description, **kwargs):
        db.Model.__init__(
            self,
            user=user,
            namespace=namespace,
            body=body,
            repository=repository,
            description=description,
            **kwargs
        )
