import redis
from time import sleep

red = redis.StrictRedis(
    host='192.168.0.223',
    port=6379,
    charset="utf-8",
    decode_responses=True
)

red.set('test-key', 'test_message', 3)

for s in range(6):
    value = red.get('test-key')
    print(value)
    sleep(1)
