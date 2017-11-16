from flask import Blueprint, render_template
from blog import db
from blog.article.models import Article

article = Blueprint('article', __name__, url_prefix='/')

@article.route("/", methods=['GET'])
def home():
    articles = Article.query.all()
    return render_template('home.html', users=articles)
