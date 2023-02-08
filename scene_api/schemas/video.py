""" Video schemas """
from marshmallow import fields, Schema
from scene_api.schemas.base import BaseSchema
from scene_api.schemas.pagination import PaginationResponseSchema
from scene_api.models.video import Video


class VideoSchema(BaseSchema):
    """Schema for a video"""

    vote_count = fields.Int(dump_only=True)

    class Meta(BaseSchema.Meta):
        model = Video


class VideosSchema(Schema):
    meta = fields.Nested(PaginationResponseSchema(context={"path": "videos"}))
    data = fields.Nested(VideoSchema(many=True))


class VideoUploadRequestSchema(Schema):
    """Schema for video file upload request"""

    file = fields.Raw(type="file", required=True)


class VideoUploadResponseSchema(Schema):
    """Schema for video file upload response"""

    file = fields.Str(dump_only=True)
