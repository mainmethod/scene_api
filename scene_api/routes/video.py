from flask import Blueprint, request
from webargs.flaskparser import use_args

from scene_api.models.video import Video
from scene_api.schemas.video import video_schema, videos_schema

blueprint = Blueprint("video_blueprint", __name__, url_prefix="/videos")


@blueprint.route("/", methods=("GET", "OPTIONS"))
def list():
    """List all videos"""
    videos = Video.query.all()
    return videos_schema.dump(videos)


@blueprint.route("/", methods=("POST",))
@use_args(video_schema)
def create(args):
    """Create a video"""
    video = Video.save(args)
    return video_schema.dump(video)
