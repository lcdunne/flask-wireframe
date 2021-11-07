import os
from dotenv import load_dotenv
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

logging.basicConfig(
    format='[%(asctime)s] - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()

# Register extensions
db = SQLAlchemy()
migrate = Migrate(compare_type=True)

# Import the models
from .models import *

def ensure_config(cfg=None):
    if cfg is None:
        load_dotenv()
        cfg = os.environ.get('FLASK_CONFIG', 'DevNative')

    logger.info(f"Loading {cfg} configuration.")

    if not cfg.startswith('config.'):
        cfg = 'config.' + cfg

    return cfg



def create_app(cfg=None):

    app = Flask(__name__)

    cfg = ensure_config(cfg)

    app.config.from_object(cfg)

    db.init_app(app)
    migrate.init_app(app, db=db)

    from app.home import home_blueprint as home

    # Add more bluprints here
    for bp in [home]:
        app.register_blueprint(bp)
    
    return app
