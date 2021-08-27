import time
from . import celery
from flask import current_app

@celery.task(name='app.tasks.do_stuff')
def do_celery_task():
    print("Sleeping...")
    time.sleep(5)
    print("Done")