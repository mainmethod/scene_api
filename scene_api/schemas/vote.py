""" Vote schemas """
from marshmallow import fields, Schema
from scene_api.schemas.base import BaseSchema
from scene_api.schemas.pagination import PaginationResponseSchema
from scene_api.models.vote import Vote


class VoteSchema(BaseSchema):
    """Schema for a vote"""

    video = fields.Nested("VideoSchema", only=("name", "url"), dump_only=True)

    class Meta(BaseSchema.Meta):
        model = Vote
        include_fk = True


class VotesSchema(Schema):
    meta = fields.Nested(PaginationResponseSchema(context={"path": "votes"}))
    data = fields.Nested(VoteSchema(many=True))
