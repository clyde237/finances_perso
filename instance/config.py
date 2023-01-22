class Config(object):
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + 'path/to/your/local/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
