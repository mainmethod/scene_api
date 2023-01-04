from scene_api.extensions import db


class BaseModel(db.Model):
    """Base SQLAlchemy model"""

    __abstract__ = True

    def save(self) -> db.Model:
        """persist video"""
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            raise e


class Video(BaseModel):
    """SQLAlchemy model for Videos"""

    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String, nullable=False)
    votes = db.relationship("Vote", back_populates="video", lazy="joined")


class Vote(BaseModel):
    """SQLAlchemy model for Votes"""

    __tablename__ = "vote"
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey("video.id"))
    voter_email = db.Column(db.String, nullable=False)
    video = db.relationship("Video", back_populates="votes", lazy="joined")
