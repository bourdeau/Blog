from flask import Blueprint, render_template, abort, redirect
from flask_security import login_required
from app import db
from app.front.models import Article
from app.admin.forms import ArticleForm

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')


@admin.route("/", methods=['GET'])
@login_required
def home():
    articles = Article.query.all()
    if not articles:
        abort(404)

    return render_template('index.html', articles=articles)


@admin.route('/article', methods=['GET', 'POST'])
@login_required
def new_article():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article = Article(form.title.data, form.content.data)
        db.session.add(new_article)
        db.session.commit()
        return redirect('/admin')

    return render_template('article.html', title='New Article', form=form)


@admin.route('/article/<id>', methods=['GET', 'POST'])
@login_required
def edit_article(id):
    article = Article.query.get(id)
    if not article:
        abort(404)

    form = ArticleForm()

    if form.validate_on_submit():
        new_article = Article(form.title.data, form.content.data)
        db.session.add(new_article)
        db.session.commit()
        return redirect('/admin')

    return render_template('article.html', title='Edit Article', form=form)
