from celery import Celery

app = Celery("task")
app.config_from_object("celeryconfig")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
