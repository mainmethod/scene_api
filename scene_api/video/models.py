""" Video model and schemas """
from scene_api.extensions import db, marshmallow
from scene_api.base.models import BaseModel, BaseSchema


class Video(BaseModel):
    """SQLAlchemy model for Videos"""

    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)


class VideoSchema(BaseSchema):
    """Schema for a video"""

    class Meta(BaseSchema.Meta):
        model = Video


video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)
