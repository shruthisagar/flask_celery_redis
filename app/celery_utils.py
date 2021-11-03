def init_celery(celery, app):
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class contextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = contextTask
