import pathlib
from flask import Flask
from scene_api.extensions import (
    db,
    marshmallow,
    migrate,
)
from scene_api import routes


def create_app():
    """Create application factory."""
    basedir = pathlib.Path(__file__).parent.resolve()
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'scene_app.db'}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(routes.video.blueprint)
    return None
