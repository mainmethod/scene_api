from flask import Blueprint
from webargs.flaskparser import use_args
from werkzeug.utils import secure_filename

from scene_api.decorators.auth import requires_auth
from scene_api.exceptions.errors import VideoUploadError
from scene_api.models.video import Video
from scene_api.schemas.pagination import PaginationSchema
from scene_api.schemas.video import (
    VideoUploadRequestSchema,
    VideoUploadResponseSchema,
    VideoSchema,
    VideosSchema,
)
from scene_api.services.uploader import send_to_s3

blueprint = Blueprint("video_blueprint", __name__, url_prefix="/videos")


@blueprint.route("/", methods=("GET", "OPTIONS"))
@use_args(PaginationSchema, location="query")
@requires_auth
def list(args):
    """List all videos"""
    videos = Video.query.filter(Video.deleted_on == None).paginate(
        page=args.get("page"), per_page=args.get("per_page")
    )
    context = {"args": args, "url_prefix": blueprint.url_prefix}
    return VideosSchema(context=context).dump({"meta": videos, "data": videos})


@blueprint.route("/", methods=("POST",))
@use_args(VideoSchema)
@requires_auth
def create(args):
    """Create a video"""
    video = Video.save(args)
    return VideoSchema().dump(video), 201


@blueprint.route("/upload", methods=("POST",))
@use_args(VideoUploadRequestSchema, location="files")
@requires_auth
def upload(args):
    """Upload video to s3"""

    file = args["file"]

    file.filename = secure_filename(file.filename)
    try:
        file_response = send_to_s3(file)
    except VideoUploadError as error:
        raise error
    return VideoUploadResponseSchema().dump({"file": file_response}), 201
