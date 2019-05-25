import click
from app.application import db
from app.admin.models import User
from sqlalchemy_utils import database_exists, create_database
from flask import current_app


@click.command()
def load_fixtures():
    """ Create the database and load the fixtures """
    db_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(db_uri):
        create_database(db_uri)
    else:
        db.drop_all()

    db.create_all()

    # Fixtures
    user = User()
    user.email = 'phbasic@gmail.com'
    user.password = '123456789'
    user.active = True
    db.session.add(user)
    db.session.commit()

    print('Initialized the database.')
