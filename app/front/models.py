import datetime
from slugify import slugify
from app import db


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    slug = db.Column(db.String(80), unique=True)
    content = db.Column(db.String(120), unique=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return '<Article %r>' % self.title

    def get_archives():
        query = 'SELECT COUNT(*) as nb, DATE_FORMAT(created_at, "%%M %%Y") as date, DATE_FORMAT(created_at, "%%Y-%%m") as date_format FROM blog.article group by DATE_FORMAT(created_at, "%%M %%Y")'
        return db.engine.execute(query)

    @classmethod
    def __declare_last__(cls):
        db.event.listen(cls, 'before_insert', cls._before_insert)
        db.event.listen(cls, 'before_update', cls._before_update)

    @staticmethod
    def _before_insert(mapper, connection, target):
        """
        @todo improve with db fetch for existing article slug
        """
        target.slug = slugify(target.title)

    @staticmethod
    def _before_update(mapper, connection, target):
        target.updated_at = datetime.utcnow()
