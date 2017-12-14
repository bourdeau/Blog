from flask import Blueprint, render_template, abort
from blog import db
from blog.article.models import Article
from datetime import datetime
from datetime import timedelta

article = Blueprint('article', __name__)

@article.route("/", methods = ['GET'])
def home():
    articles = Article.query.all()

    return render_template('article/home.html', articles=articles)

@article.route("/<slug>", methods = ['GET'])
def single(slug):
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        abort(404)

    return render_template('article/single.html', article=article)


@article.route("/archives/<date>", methods = ['GET'])
def archives(date):
    date_from = datetime.strptime(date, '%Y-%m')
    date_to = date_from + timedelta(days=30)

    date_from_string = date_from.strftime("%Y-%m-%d %H:%M:%S")
    date_to_string = date_to.strftime("%Y-%m-%d %H:%M:%S")

    articles = Article.query.filter(Article.created_at.between(date_from_string, date_to_string))

    return render_template('article/archives.html', articles=articles, date_from=date_from)

@article.context_processor
def archives():
    archives = Article.get_archives()

    return dict(archives=archives)
