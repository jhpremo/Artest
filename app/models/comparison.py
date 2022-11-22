from .db import db, environment, SCHEMA, add_prefix_for_prod

class Comparison(db.Model):
    __tablename__ = 'comparisons'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    title = db.Column(db.String(75), nullable=False)
    work_1_title = db.Column(db.String(75), nullable=False)
    work_1_artist = db.Column(db.String(75), nullable=False)
    work_1_image_url = db.Column(db.String(2048), nullable=False)
    work_1_display_date = db.Column(db.String(50), nullable=False)
    work_1_marker_obj = db.Column(db.JSON, nullable=True)
    work_2_title = db.Column(db.String(75), nullable=False)
    work_2_artist = db.Column(db.String(75), nullable=False)
    work_2_image_url = db.Column(db.String(2048), nullable=False)
    work_2_display_date = db.Column(db.String(50), nullable=False)
    work_2_marker_obj = db.Column(db.JSON, nullable=True)
    comparison_text = db.Column(db.String(3000), nullable=True)

    user = db.relationship('User', back_populates='comparisons')

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "title": self.title,
            "workOneTitle": self.work_1_title,
            "workOneArtist": self.work_1_artist,
            "workOneImageUrl": self.work_1_image_url,
            "workOneDisplayDate": self.work_1_display_date,
            "workOneMarkerObj": self.work_1_marker_obj,
            "workTwoTitle": self.work_2_title,
            "workTwoArtist": self.work_2_artist,
            "workTwoImageUrl": self.work_2_image_url,
            "workTwoDisplayDate": self.work_2_display_date,
            "workTwoMarkerObj": self.work_2_marker_obj,
            "comparisonText": self.comparison_text
        }
