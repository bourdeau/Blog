import os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# General Flask
THREADS_PER_PAGE = 2
DEBUG = os.getenv("DEBUG")

# Database
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE)

print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}
FIXTURES_DIRS = BASE_DIR + '/fixtures'

# Security
SECRET_KEY = os.getenv("SECRET_KEY")
CSRF_SESSION_KEY = os.getenv("CSRF_SESSION_KEY")
CSRF_ENABLED = True

# Security (flask_security: http://pythonhosted.org/Flask-Security/configuration.html)
SECURITY_REGISTER_URL = '/register'
SECURITY_LOGIN_URL = '/login'
SECURITY_RESET_URL = '/reset'
SECURITY_REGISTERABLE = False
SECURITY_PASSWORD_HASH = os.getenv("SECURITY_PASSWORD_HASH")
SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")