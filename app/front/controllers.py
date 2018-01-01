from app.blueprints import front
from flask import render_template, abort, request
from app.front.models import Article
from datetime import datetime, timedelta


@front.route("/", methods=['GET'])
def home():
    nb_record = 3

    page = request.args.get('page')

    if not page:
        page = 1
    else:
        page = int(page)

    record_query = Article.query.paginate(page, nb_record, False)
    articles = record_query.items
    total = record_query.total

    more_records = True

    if (nb_record * page) >= total:
        more_records = False

    pagination = {
        'next_page': page + 1,
        'previous_page': page - 1,
        'more_records': more_records
    }

    return render_template('home.html', articles=articles, pagination=pagination)


@front.route("/<slug>", methods=['GET'])
def single(slug):
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        abort(404)

    return render_template('single.html', article=article)


@front.route("/archives/<date>", methods=['GET'])
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
