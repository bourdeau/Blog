from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore

# Define the WSGI application object
app = Flask(__name__)

# Configuration from config.py
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Setup Flask-Security
from app.admin.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.cli.command('initdb')
def initdb_command():
    db.create_all()
    """
    Fixtures
    """
    user = User()
    user.email = 'phbasic@gmail.com'
    user.password = '123456789'
    user.active = True
    db.session.add(user)
    db.session.commit()

    print('Initialized the database.')


@app.errorhandler(404)
def not_found_404(error):
    return render_template('common/404.html'), 404


@app.errorhandler(500)
def not_found_500(error):
    return render_template('common/500.html'), 500

# Import a module / component using its blueprint handler variable
from app.front.controllers import front
from app.admin.controllers import admin

# Register blueprint(s)
app.register_blueprint(front)
app.register_blueprint(admin)
