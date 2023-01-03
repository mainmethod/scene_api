from scene_api.extensions import db, marshmallow


class BaseModel(db.Model):
    """Base SQLAlchemy model"""

    __abstract__ = True

    def save(self) -> db.Model:
        """persist video"""
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            raise e


class BaseSchema(marshmallow.SQLAlchemyAutoSchema):
    """Schema for a video"""

    class Meta:
        load_instance = True
        sqla_session = db.session
