from flask import Blueprint, render_template
from blog import db
from blog.article.models import Article

article = Blueprint('article', __name__)

@article.route("/", methods = ['GET'])
def home():
    articles = Article.query.all()
    return render_template('home.html', articles=articles)

@article.route("/<id>", methods = ['GET'])
def single(id):
    article = Article.query.filter_by(id=id).first()
    if not article:
        return render_template('404.html'), 404

    return render_template('single.html', article=article)
