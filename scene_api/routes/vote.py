from flask import Blueprint
from webargs.flaskparser import use_args

from scene_api.models.vote import Vote
from scene_api.schemas.pagination import pagination_schema
from scene_api.schemas.vote import vote_schema, votes_schema

blueprint = Blueprint("vote_blueprint", __name__, url_prefix="/votes")


@blueprint.route("/", methods=("GET", "OPTIONS"))
@use_args(pagination_schema, location="query")
def list(args):
    """List all videos"""
    videos = Vote.query.paginate(page=args.get("page"), per_page=args.get("per_page"))
    return votes_schema.dump(videos)


@blueprint.route("/", methods=("POST",))
@use_args(vote_schema)
def create(args):
    """Create a vote"""
    vote = Vote.save(args)
    return vote_schema.dump(vote), 201
