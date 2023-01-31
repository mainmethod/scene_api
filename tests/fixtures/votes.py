import pytest
from scene_api.models.vote import Vote


@pytest.fixture
def vote():
    return Vote(id=1, vote_email="some-email@email.com", video_id=1)


@pytest.fixture
def vote_request():
    return {"video_id": 1, "voter_email": "some-email@email.com"}
