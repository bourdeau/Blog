import datetime
from slugify import slugify
from app.application import db


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    slug = db.Column(db.String(80), unique=True)
    content = db.Column(db.UnicodeText(), unique=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.title

    def get_archives():
        query = 'SELECT COUNT(*) as nb, DATE_FORMAT(created_at, "%%M %%Y") as date, DATE_FORMAT(created_at, "%%Y-%%m") as date_format FROM blog_db.article group by DATE_FORMAT(created_at, "%%M %%Y")'
        return db.engine.execute(query)

    @classmethod
    def __declare_last__(cls):
        db.event.listen(cls, 'before_insert', cls._before_insert)
        db.event.listen(cls, 'before_update', cls._before_update)

    @staticmethod
    def _before_insert(mapper, connection, target):
        """
        Slug article before insert
        """
        new_slug = slugify(target.title)
        nb_existing_titles = target.query.filter_by(title=target.title).count()
        if nb_existing_titles == 0:
            target.slug = new_slug
        else:
            nb_existing_titles += 1
            target.slug = new_slug + '-' + str(nb_existing_titles)

    @staticmethod
    def _before_update(mapper, connection, target):
        target.updated_at = datetime.datetime.now()
