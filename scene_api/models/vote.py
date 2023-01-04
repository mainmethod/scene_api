""" Vote model """
from scene_api.extensions import db
from scene_api.models.base import BaseModel


class Vote(BaseModel):
    """SQLAlchemy model for Votes"""

    __tablename__ = "vote"
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey("video.id"))
    voter_email = db.Column(db.String, nullable=False)
    video = db.relationship("Video", lazy="joined")
