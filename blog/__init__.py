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
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from blog.article.controllers import article

# Register blueprint(s)
blog.register_blueprint(article)
# blog.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()
