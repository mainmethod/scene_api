""" Video schemas """
from marshmallow import fields, Schema
from scene_api.schemas.base import BaseSchema
from scene_api.models.video import Video


class VideoSchema(BaseSchema):
    """Schema for a video"""

    vote_count = fields.Int(dump_only=True)

    class Meta(BaseSchema.Meta):
        model = Video


video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)


class VideoUploadRequestSchema(Schema):
    """Schema for video file upload request"""

    file = fields.Raw(type="file", required=True)


video_upload_request_schema = VideoUploadRequestSchema()


class VideoUploadResponseSchema(Schema):
    """Schema for video file upload response"""

    file = fields.Str(dump_only=True)


video_upload_response_schema = VideoUploadResponseSchema()
