from celery import Celery
from flask import Flask
import os
from .celery_utils import init_celery
PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]

def make_celery(app_name=__name__):
    redis_uri = "redis://localhost:6379"
    return Celery(app_name, backend=redis_uri, broker=redis_uri)


celery = make_celery()

def create_app(app_name=PKG_NAME, **kwargs):
    app = Flask(app_name)
    if kwargs.get("celery"):
        init_celery(kwargs.get("celery"), app)
    from sample_module.sample_view import bp
    app.register_blueprint(bp)
    return app


