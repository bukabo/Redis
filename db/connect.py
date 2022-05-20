from constant import redis_con
import redis


con = redis.StrictRedis(
    host=redis_con['host'],
    port=redis_con['port'],
    charset="utf-8",
    decode_responses=True
)