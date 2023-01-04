""" Vote schemas """
from marshmallow_sqlalchemy import fields
from scene_api.schemas.base import BaseSchema
from scene_api.models.vote import Vote


class VoteSchema(BaseSchema):
    """Schema for a vote"""

    video = fields.Nested("VideoSchema", only=("name", "url"), dump_only=True)

    class Meta(BaseSchema.Meta):
        model = Vote
        include_fk = True


vote_schema = VoteSchema()
votes_schema = VoteSchema(many=True)
