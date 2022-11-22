from .db import db, environment, SCHEMA, add_prefix_for_prod

class Set(db.Model):
    __tablename__ = 'sets'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    title = db.Column(db.String(75), nullable=False)

    user = db.relationship('User', back_populates='sets')
    cards = db.relationship('SetCard', back_populates='card_set', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "title": self.title
        }
