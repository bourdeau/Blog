from flask import Blueprint

front = Blueprint('front', 'app.front.controllers', template_folder='templates')
admin = Blueprint('admin', 'app.admin.controllers', url_prefix='/admin', template_folder='templates')

all_blueprints = (front, admin)
