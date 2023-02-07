from flask import Blueprint
from webargs.flaskparser import use_args
from werkzeug.utils import secure_filename
from scene_api.exceptions.errors import VideoUploadError
from scene_api.schemas.pagination import pagination_schema
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
@use_args(pagination_schema, location="query")
def list(args):
    """List all videos"""
    videos = Video.query.filter(Video.deleted_on == None).paginate(
        page=args.get("page"), per_page=args.get("per_page")
    )
    return videos_schema.dump(videos)


@blueprint.route("/", methods=("POST",))
@use_args(video_schema)
def create(args):
    """Create a video"""
    video = Video.save(args)
    return video_schema.dump(video), 201


@blueprint.route("/upload", methods=("POST",))
@use_args(video_upload_request_schema, location="files")
def upload(args):
    """Upload video to s3"""

    file = args["file"]

    file.filename = secure_filename(file.filename)
    try:
        file_response = send_to_s3(file)
    except VideoUploadError as error:
        raise error
    return video_upload_response_schema.dump({"file": file_response}), 201
