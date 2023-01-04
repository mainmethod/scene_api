from scene_api.extensions import db


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
