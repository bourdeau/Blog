from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore

# Define the WSGI application object
blog = Flask(__name__)

# Configuration from config.py
blog.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(blog)
migrate = Migrate(blog, db)

# Setup Flask-Security
from blog.admin.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(blog, user_datastore)

# HTTP error handling
@blog.errorhandler(404)
def not_found_404(error):
    return render_template('common/404.html'), 404

@blog.errorhandler(500)
def not_found_500(error):
    return render_template('common/500.html'), 500

# Import a module / component using its blueprint handler variable
from blog.front.controllers import front
from blog.admin.controllers import admin

# Register blueprint(s)
blog.register_blueprint(front)
blog.register_blueprint(admin)
