import os
from app import create_app


app = create_app(os.environ.get('FLASK_CONFIG'))

if __name__ == '__main__':
    # Starting rabbitmq: docker run --name rabbitmq -p 5672:5672 -p 15672:15672 -d rabbitmq:3-management
    # Running celery: celery -A celery_worker.celery worker --loglevel=info
    app.run(host=app.config.get('HOST'))