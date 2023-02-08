from flask import Flask
from scene_api.extensions import (
    db,
    marshmallow,
    migrate,
)

# from scene_api.api.routes import video_blueprint, vote_blueprint
from scene_api import routes


def create_app():
    """Create application factory."""

    app = Flask(__name__)

    app.config.from_pyfile("settings.py")

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
    app.register_blueprint(routes.errors.blueprint)
    app.register_blueprint(routes.video.blueprint)
    app.register_blueprint(routes.vote.blueprint)
    return None
