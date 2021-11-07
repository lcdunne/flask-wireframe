import os
from dotenv import load_dotenv
from app import create_app

load_dotenv()
cfg = os.environ.get('FLASK_CONFIG', 'DevNative')

app = create_app(cfg)

host = app.config.get('HOST') # If None, runs on localhost
debug = app.config.get('DEBUG', True)



if __name__ == '__main__':
    app.run(host=host, debug=debug)