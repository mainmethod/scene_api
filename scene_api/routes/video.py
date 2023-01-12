from flask import Blueprint, request
from webargs.flaskparser import use_args
from werkzeug.utils import secure_filename

from scene_api.decorators.auth import requires_auth
from scene_api.models.video import Video
from scene_api.schemas.video import (
    video_upload_request_schema,
    video_upload_response_schema,
    video_schema,
    videos_schema,
)
from scene_api.services.uploader import send_to_s3

blueprint = Blueprint("video_blueprint", __name__, url_prefix="/videos")


@blueprint.route("/", methods=("GET", "OPTIONS"))
@requires_auth
def list():
    """List all videos"""
    videos = Video.query.filter(Video.deleted_on == None).all()
    return videos_schema.dump(videos)


@blueprint.route("/", methods=("POST",))
@use_args(video_schema)
@requires_auth
def create(args):
    """Create a video"""
    video = Video.save(args)
    return video_schema.dump(video)


@blueprint.route("/upload", methods=("POST",))
@use_args(video_upload_request_schema, location="files")
@requires_auth
def upload(args):
    """Upload video to s3"""

    file = args["file"]

    file.filename = secure_filename(file.filename)
    file_response = send_to_s3(file)
    return video_upload_response_schema.dump({"file": file_response})
