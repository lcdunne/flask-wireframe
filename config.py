import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    DEBUG = False
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tbl.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///tbl.db')
    print("\nUsing ", SQLALCHEMY_DATABASE_URI.split(':')[0], "database.\n")