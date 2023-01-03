from scene_api.extensions import db, marshmallow


class Video(db.Model):
    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
                return self
            except Exception as e:
                db.session.rollback()
                raise e


class VideoSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Video
        load_instance = True
        sqla_session = db.session


video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)
