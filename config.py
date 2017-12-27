import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:h1n1h5n1SB@localhost/blog'
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 2
CSRF_ENABLED     = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_SESSION_KEY = "mLLJXWoXzs9ZkLxQVN7tDBWv2WwNKlZyRXhs3lKYhpQ="
SECRET_KEY = "XZ0F7nAf1o9dfLaJDDvpIcBAThR/DNlIHTDowaSa+uM="

# Security (flask_security: http://pythonhosted.org/Flask-Security/configuration.html)
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'kuahduiahzd'
SECURITY_REGISTERABLE = False
SECURITY_REGISTER_URL = '/register'
SECURITY_LOGIN_URL = '/login'
SECURITY_RESET_URL = '/reset'
