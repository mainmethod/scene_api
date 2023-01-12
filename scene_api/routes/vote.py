from flask import Blueprint
from webargs.flaskparser import use_args

from scene_api.decorators.auth import requires_auth
from scene_api.models.vote import Vote
from scene_api.schemas.vote import vote_schema, votes_schema

blueprint = Blueprint("vote_blueprint", __name__, url_prefix="/votes")


@blueprint.route("/", methods=("GET", "OPTIONS"))
@requires_auth
def list():
    """List all videos"""
    videos = Vote.query.all()
    return votes_schema.dump(videos)


@blueprint.route("/", methods=("POST",))
@use_args(vote_schema)
@requires_auth
def create(args):
    """Create a vote"""
    vote = Vote.save(args)
    return vote_schema.dump(vote)
