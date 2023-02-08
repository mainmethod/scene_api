from flask import Blueprint
from webargs.flaskparser import use_args

from scene_api.models.vote import Vote
from scene_api.schemas.pagination import PaginationSchema
from scene_api.schemas.vote import VoteSchema, VotesSchema

blueprint = Blueprint("vote_blueprint", __name__, url_prefix="/votes")


@blueprint.route("/", methods=("GET", "OPTIONS"))
@use_args(PaginationSchema, location="query")
def list(args):
    """List all videos"""
    votes = Vote.query.paginate(page=args.get("page"), per_page=args.get("per_page"))
    context = {"args": args, "url_prefix": blueprint.url_prefix}
    return VotesSchema(context=context).dump({"meta": votes, "data": votes})


@blueprint.route("/", methods=("POST",))
@use_args(VoteSchema)
def create(args):
    """Create a vote"""
    vote = Vote.save(args)
    return VoteSchema().dump(vote), 201
