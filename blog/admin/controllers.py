from flask import Blueprint
from blog import db
from blog.front.models import Article
from flask_security import login_required


admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

@admin.route("/", methods = ['GET'])
@login_required
def home():
    articles = Article.query.all()
    if not articles:
        abort(404)

    return render_template('index.html', articles=articles)
