import pytest
from scene_api.models.video import Video


@pytest.fixture
def video():
    return Video(id=1, name="test video", url="https://testvideo.com/video/1")


@pytest.fixture
def video_request():
    return {"name": "test video", "url": "https://testvideo.com/video/1"}
