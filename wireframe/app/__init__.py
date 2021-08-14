import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Register extensions
db = SQLAlchemy()
migrate = Migrate(compare_type=True)

# Import the models
from .models import *

def create_app(cfg=None):
    app = Flask(__name__)

    if cfg is None:
        # Try to get from config
        load_dotenv()
        cfg = os.environ.get('FLASK_CONFIG', 'config.BaseConfig')

    print("Loading config: ", cfg)
    app.config.from_object(cfg)

    db.init_app(app)
    migrate.init_app(app, db=db)

    from app.home import home_blueprint as home

    # Add more bluprints here
    for bp in [home]:
        app.register_blueprint(bp)
    
    return app
