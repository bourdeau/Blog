from app.blueprints import admin
from flask import render_template, abort, redirect
from flask_security import login_required
from app.application import db
from app.front.models import Article
from app.admin.forms import ArticleForm


@admin.route("/", methods=['GET'])
@login_required
def home():
    articles = Article.query.all()

    return render_template('index.html', articles=articles)


@admin.route('/article', methods=['GET', 'POST'])
@admin.route('/article/<id>', methods=['GET', 'POST'])
@login_required
def article(id=None):
    """
    Create or Update an article
    """

    if id:
        article = Article.query.get(id)
        if not article:
            abort(404)
    else:
        article = Article()

    form = ArticleForm(obj=article)
    if form.validate_on_submit():
        form.populate_obj(article)

        db.session.add(article)
        db.session.commit()
        return redirect('/admin')

    return render_template('article.html', title='New Article', form=form)


@admin.route('/article/delete/<id>', methods=['GET'])
@login_required
def delete_article(id):
    """
    Delete an Article
    """
    article = Article.query.get(id)
    if not article:
        abort(404)

    db.session.delete(article)
    db.session.commit()

    return redirect('/admin')
