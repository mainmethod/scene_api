""" Video schemas """
from marshmallow import fields
from marshmallow_sqlalchemy.fields import Nested
from scene_api.schemas.base import BaseSchema
from scene_api.models.video import Video


class VideoSchema(BaseSchema):
    """Schema for a video"""

    vote_count = fields.Int(dump_only=True)

    class Meta(BaseSchema.Meta):
        model = Video


video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)
