class SceneApiError(Exception):
    """Base class for Scene API errors"""

    status = 500
    code = "scene_api_error"
    description = "An API error has occured"

    def __init__(self, code=None, description=None, status=None):
        if code:
            self.code = code
        if description:
            self.description = description
        if status:
            self.status = status


class VideoUploadError(SceneApiError):
    status = 400
    code = "scene_api_upload_error"
    description = "There was a problem with the video upload"
