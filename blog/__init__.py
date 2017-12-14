from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Define the WSGI application object
blog = Flask(__name__)

# Configuration from config.py
blog.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(blog)
migrate = Migrate(blog, db)

# HTTP error handling
@blog.errorhandler(404)
def not_found_404(error):
    return render_template('common/404.html'), 404

@blog.errorhandler(500)
def not_found_500(error):
    return render_template('common/500.html'), 500

# Import a module / component using its blueprint handler variable
from blog.article.controllers import article

# Register blueprint(s)
blog.register_blueprint(article)
# blog.register_blueprint(xyz_module)
# ..
