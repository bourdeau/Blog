from flask import Blueprint, render_template
from blog import db
from blog.article.models import Article

article = Blueprint('article', __name__)

@article.route("/", methods = ['GET'])
def home():
    articles = Article.query.all()
    return render_template('article/home.html', articles=articles)

@article.route("/<slug>", methods = ['GET'])
def single(slug):
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        return render_template('404.html'), 404

    return render_template('article/single.html', article=article)


@article.context_processor
def archives():
    archives = Article.get_archives()
    return dict(archives=archives)
