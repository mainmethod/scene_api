from scene_api.extensions import db, marshmallow


class BaseSchema(marshmallow.SQLAlchemyAutoSchema):
    """Base Schema"""

    class Meta:
        load_instance = True
        sqla_session = db.session
