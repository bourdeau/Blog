from flask import Blueprint, render_template, abort
from app import db
from app.front.models import Article
from datetime import datetime, timedelta

front = Blueprint('front', __name__, template_folder='templates')


@front.route("/", methods = ['GET'])
def home():
    articles = Article.query.all()

    return render_template('home.html', articles=articles)


@front.route("/<slug>", methods = ['GET'])
def single(slug):
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        abort(404)

    return render_template('single.html', article=article)


@front.route("/archives/<date>", methods = ['GET'])
def archives(date):
    date_from = datetime.strptime(date, '%Y-%m')
    date_to = date_from + timedelta(days=30)

    date_from_string = date_from.strftime("%Y-%m-%d %H:%M:%S")
    date_to_string = date_to.strftime("%Y-%m-%d %H:%M:%S")

    articles = Article.query.filter(Article.created_at.between(date_from_string, date_to_string))

    return render_template('archives.html', articles=articles, date_from=date_from)


@front.context_processor
def archives_get():
    archives = Article.get_archives()

    return dict(archives=archives)
