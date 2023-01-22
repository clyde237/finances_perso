from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from .mybudget import bp as mybudget_bp

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)

from mybudget import routes, models

if __name__ == '__main__':
    app.register_blueprint(mybudget_bp)
    app.run()
