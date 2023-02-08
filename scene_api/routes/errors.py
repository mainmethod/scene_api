from flask import Blueprint, jsonify
from scene_api.exceptions.errors import SceneApiError
from werkzeug.exceptions import HTTPException

blueprint = Blueprint("errors", __name__)


@blueprint.app_errorhandler(SceneApiError)
def handle_scene_api_error(e):
    return (
        jsonify({"code": e.code, "description": e.description, "status": e.status}),
        e.status,
    )


@blueprint.app_errorhandler(Exception)
def handle_error(e):
    status = 500
    if isinstance(e, HTTPException):
        status = e.code
    return (
        jsonify(
            {"code": "unhandled_exception", "description": str(e), "status": status}
        ),
        status,
    )
