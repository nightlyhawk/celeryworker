import os

CELERY_BROKER_URL = os.getenv("BROKER_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.getenv("RESULT_BACKEND", "redis://redis:6379/0")
