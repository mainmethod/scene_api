import pathlib

basedir = pathlib.Path(__file__).parent.resolve()

# db config
SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'scene_app.db'}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAX_CONTENT_LENGTH = 16 * 1000 * 1000
