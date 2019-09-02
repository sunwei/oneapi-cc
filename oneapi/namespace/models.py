import datetime as dt
from oneapi.database import (Model, Column, SurrogatePK, db, reference_col, relationship)


class Namespace(Model, SurrogatePK):
    __tablename__ = 'namespace'

    # id is needed for primary join, it does work with SurrogatePK class
    id = db.Column(db.Integer, primary_key=True)

    user_id = reference_col('users', nullable=False)
    user = relationship('User', backref=db.backref('namespaces'))

    name = Column(db.String(50), nullable=True)
    createdAt = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updatedAt = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, user, name, **kwargs):
        db.Model.__init__(self, user=user, name=name, **kwargs)
