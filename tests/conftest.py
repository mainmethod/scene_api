import pytest
from glob import glob
from scene_api.app import create_app


pytest_plugins = [
    fixture_file.replace("/", ".").replace(".py", "")
    for fixture_file in glob("tests/fixtures/[!__]*.py", recursive=True)
]


@pytest.fixture()
def client():
    app = create_app()

    client = app.test_client()

    yield client
