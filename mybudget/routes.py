from flask import Blueprint

bp = Blueprint('mybudget', __name__, template_folder='templates')

from app.mybudget import views
