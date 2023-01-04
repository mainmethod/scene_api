""" Video model """
from scene_api.extensions import db
from scene_api.models.base import BaseModel


class Video(BaseModel):
    """SQLAlchemy model for Videos"""

    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
