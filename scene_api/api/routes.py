from flask import Blueprint, request
from webargs.flaskparser import use_args

from .models import Video, Vote
from .schemas import video_schema, videos_schema, vote_schema, votes_schema

video_blueprint = Blueprint("video_blueprint", __name__, url_prefix="/videos")


@video_blueprint.route("/", methods=("GET", "OPTIONS"))
def list():
    """List all videos"""
    videos = Video.query.all()
    return videos_schema.dump(videos)


@video_blueprint.route("/", methods=("POST",))
@use_args(video_schema)
def create(args):
    """Create a video"""
    video = Video.save(args)
    return video_schema.dump(video)


vote_blueprint = Blueprint("vote_blueprint", __name__, url_prefix="/votes")


@vote_blueprint.route("/", methods=("GET", "OPTIONS"))
def list():
    """List all videos"""
    videos = Vote.query.all()
    return votes_schema.dump(videos)


@vote_blueprint.route("/", methods=("POST",))
# @use_args(vote_schema)
def create():
    """Create a vote"""
    data = request.get_json(force=True)
    new_vote = vote_schema.load(data)
    vote = Vote.save(new_vote)
    return vote_schema.dump(vote)
