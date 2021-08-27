import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    DEBUG = False
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tbl.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'pyamqp://guest@localhost//'# 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'rpc://' #'redis://localhost:6379'
    

class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///tbl.db')

class DockerConfig(BaseConfig):
    HOST = '0.0.0.0'
    DEBUG=True
    print("DockerConfig")

class TestConfig(BaseConfig):
    DEBUG = True