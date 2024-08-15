import os

broker_url = os.getenv("BROKER_URL", "redis://redis:6379/0")
result_backend = os.getenv("RESULT_BACKEND", "redis://redis:6379/0")