import mock
import json


def test__get_videos(client):
    response = client.get("/videos/", content_type="application/json")
    assert response.status_code == 200


def test__post_videos(client, video_request):
    response = client.post(
        "/videos/", content_type="application/json", data=json.dumps(video_request)
    )
    assert response.status_code == 201


def test__get_votes(client):
    response = client.get("/votes/", content_type="application/json")
    assert response.status_code == 200


def test__post_votes(client, vote_request):
    response = client.post(
        "/votes/", content_type="application/json", data=json.dumps(vote_request)
    )
    assert response.status_code == 201
