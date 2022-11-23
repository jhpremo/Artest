from .db import db, environment, SCHEMA, add_prefix_for_prod

class SetCard(db.Model):
    __tablename__ = 'set_cards'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('sets.id')))
    title = db.Column(db.String(75), nullable=False)
    artist = db.Column(db.String(75), nullable=False)
    image_url = db.Column(db.String(2048), nullable=False)
    display_date = db.Column(db.String(50), nullable=False)
    marker_obj = db.Column(db.JSON, nullable=True)
    notes = db.Column(db.String(1000), nullable=True)

    card_set = db.relationship('Set', back_populates='cards')

    def to_dict(self):
        return {
            "id": self.id,
            "setId": self.set_id,
            "title": self.title,
            "artist": self.artist,
            "imageUrl": self.image_url,
            "markerObj": self.marker_obj,
            "notes": self.notes
        }
