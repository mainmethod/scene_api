from flask import Blueprint, request
from .models import Video, video_schema, videos_schema

blueprint = Blueprint("video_blueprint", __name__, url_prefix="/videos")


@blueprint.route("/", methods=("GET", "OPTIONS"))
def list():
    videos = Video.query.all()
    return videos_schema.dump(videos)


@blueprint.route("/", methods=("POST",))
def create():
    video_json = request.get_json(force=True)
    new_video = video_schema.load(video_json)
    video = Video.save(new_video)
    return video_schema.dump(video)
