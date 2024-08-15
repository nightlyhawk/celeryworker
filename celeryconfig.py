import os

# host = os.environ('UPSTASH_REDIS_HOST')
# password = os.environ('UPSTASH_REDIS_PASSWORD')
# port = os.environ('UPSTASH_REDIS_PORT')

broker_url =os.getenv('BROKER_URL')
result_backend = os.getenv('RESULT_BACKEND')
