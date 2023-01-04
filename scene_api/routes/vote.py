from flask import Blueprint, request
from webargs.flaskparser import use_args

from scene_api.models.vote import Vote
from scene_api.schemas.vote import vote_schema, votes_schema

blueprint = Blueprint("vote_blueprint", __name__, url_prefix="/votes")


@blueprint.route("/", methods=("GET", "OPTIONS"))
def list():
    """List all videos"""
    videos = Vote.query.all()
    return votes_schema.dump(videos)


@blueprint.route("/", methods=("POST",))
# @use_args(vote_schema)
def create():
    """Create a vote"""
    data = request.get_json(force=True)
    new_vote = vote_schema.load(data)
    vote = Vote.save(new_vote)
    return vote_schema.dump(vote)
