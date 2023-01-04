""" Video schemas """
from scene_api.schemas.base import BaseSchema
from scene_api.models.video import Video


class VideoSchema(BaseSchema):
    """Schema for a video"""

    class Meta(BaseSchema.Meta):
        model = Video


video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)
