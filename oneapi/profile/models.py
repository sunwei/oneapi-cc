from oneapi.database import (Model, Column, SurrogatePK, db, reference_col, relationship)


class UserProfile(Model, SurrogatePK):
    __tablename__ = 'userprofile'

    # id is needed for primary join, it does work with SurrogatePK class
    id = db.Column(db.Integer, primary_key=True)

    user_id = reference_col('users', nullable=False)
    user = relationship('User', backref=db.backref('profile', uselist=False))
    bio = Column(db.String(300), nullable=True)
    image = Column(db.String(120), nullable=True)

    def __init__(self, user, **kwargs):
        db.Model.__init__(self, user=user, **kwargs)

    @property
    def username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email
