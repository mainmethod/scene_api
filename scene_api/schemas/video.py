""" Video schemas """
from marshmallow_sqlalchemy import fields
from scene_api.schemas.base import BaseSchema
from scene_api.models.video import Video


class VideoSchema(BaseSchema):
    """Schema for a video"""

    votes = fields.Nested(
        "VoteSchema", many=True, only=("id", "voter_email"), dump_only=True
    )

    class Meta(BaseSchema.Meta):
        model = Video


video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)
