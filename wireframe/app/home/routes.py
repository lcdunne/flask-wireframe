from flask import render_template
from . import home_blueprint
from ..tasks import do_celery_task


@home_blueprint.route('/')
def index():
    return render_template('home.html')

@home_blueprint.route('/cel')
def do_celery():
    do_celery_task.apply_async()
    return "Doing async..."
