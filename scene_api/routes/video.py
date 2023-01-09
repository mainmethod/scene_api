from flask import Blueprint, request
from webargs.flaskparser import use_args
from werkzeug.utils import secure_filename

from scene_api.models.video import Video
from scene_api.schemas.video import video_schema, videos_schema
from scene_api.services.uploader import send_to_s3

blueprint = Blueprint("video_blueprint", __name__, url_prefix="/videos")


@blueprint.route("/", methods=("GET", "OPTIONS"))
def list():
    """List all videos"""
    videos = Video.query.filter(Video.deleted_on == None).all()
    return videos_schema.dump(videos)


@blueprint.route("/", methods=("POST",))
@use_args(video_schema)
def create(args):
    """Create a video"""
    video = Video.save(args)
    return video_schema.dump(video)


@blueprint.route("/upload", methods=("POST",))
def upload():
    """Upload video to s3"""
    if "file" not in request.files:
        return "No file key in request.files"

    file = request.files["file"]

    if file.filename == "":
        return "Please select a file"

    if file:
        file.filename = secure_filename(file.filename)
        output = send_to_s3(file)
        return str(output)

    else:
        return "no file"
