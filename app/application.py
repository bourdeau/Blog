from flask import Flask, render_template
from flask_security import SQLAlchemyUserDatastore
from importlib import import_module
from app.blueprints import all_blueprints
from app.extensions import db, migrate, security
# Must be after db because classes need db
from app.admin.models import User, Role
from app.commands import test


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errorhandlers(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

    # @todo there is no init_app in SQLAlchemyUserDatastore :'(
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)

    security.init_app(app, user_datastore)

    return None


def register_blueprints(app):
    # Registering modules
    for module in all_blueprints:
        import_module(module.import_name)
        app.register_blueprint(module)

    return None


def register_commands(app):
    app.cli.add_command(test)


def register_errorhandlers(app):
    @app.errorhandler(404)
    def not_found_404(error):
        return render_template('common/404.html'), 404

    @app.errorhandler(500)
    def not_found_500(error):
        return render_template('common/500.html'), 500
