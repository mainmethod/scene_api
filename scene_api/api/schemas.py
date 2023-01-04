from marshmallow_sqlalchemy import fields
from scene_api.extensions import db, marshmallow
from .models import Video, Vote


class BaseSchema(marshmallow.SQLAlchemyAutoSchema):
    """Base Schema"""

    class Meta:
        load_instance = True
        sqla_session = db.session


class VideoSchema(BaseSchema):
    """Schema for a video"""

    class Meta(BaseSchema.Meta):
        model = Video


video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)


class VoteSchema(BaseSchema):
    """Schema for a vote"""

    class Meta(BaseSchema.Meta):
        model = Vote
        include_fk = True


vote_schema = VoteSchema()
votes_schema = VoteSchema(many=True)
