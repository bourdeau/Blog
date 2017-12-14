from blog import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    slug = db.Column(db.String(80), unique=True)
    content = db.Column(db.String(120), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Article %r>' % self.title
