""" Video model """
from sqlalchemy import func
from scene_api.extensions import db
from scene_api.models.base import BaseModel
from scene_api.models.vote import Vote


class Video(BaseModel):
    """SQLAlchemy model for Videos"""

    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String, nullable=False)
    votes = db.relationship("Vote", back_populates="video", lazy="joined")

    @property
    def vote_count(self):
        """Get vote count for the video"""
        query = db.session.query(Vote).filter(Vote.video_id == self.id)
        count_q = query.statement.with_only_columns([func.count()]).order_by(None)
        count = query.session.execute(count_q).scalar()
        return count
