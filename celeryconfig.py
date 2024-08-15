import os

host = os.environ('UPSTASH_REDIS_HOST')
password = os.environ('UPSTASH_REDIS_PASSWORD')
port = os.environ('UPSTASH_REDIS_PORT')

broker_url = "redis://:{}@{}:{}".format(password, host, port)
result_backend = "redis://:{}@{}:{}".format(password, host, port)
