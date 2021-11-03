from app import celery, create_app
from app.celery_utils import init_celery

app = create_app()
init_celery(celery, app)
