from time import sleep
import db

red = db.con
red.set('test-key', 'test_message', 3)
red.set('int', '0')

for s in range(6):
    value = red.get('test-key')
    incr = red.incr('int')
    print(incr, value)
    # sleep(1)

red.lpush('my_list', 'A')
print(f"my_list: {red.lrange('my_list', 0, 5)}")

# Добавить вторую строку в список справа
red.rpush('my_list', 'B')
print(f"my_list: {red.lrange('my_list', 0, 1)}")

# Вставить третью строку в список справа
red.rpush('my_list', 'C')
print(f"my_list: {red.lrange('my_list', 0, 1)}")

# Удалить из списка 1 экземпляр, значение которого "C"
red.lrem('my_list', 1, 'C')
print(f"my_list: {red.lrange('my_list', 0, 1)}")

# Вставить строку в наш список слева
red.lpush('my_list', 'C')
print(f"my_list: {red.lrange('my_list', 0, 1)}")

# Вытащить первый элемент нашего списка и переместить его в конец
red.rpush('my_list', red.lpop('my_list'))
print(f"my_list: {red.lrange('my_list', 0, 1)}")

print('-' * 20)
# Добавить элемент в set 1
red.sadd('my_set_1', 'Y')
print(f"my_set_1: {red.smembers('my_set_1')}")
# Добавить элемент в set 1
red.sadd('my_set_1', 'X')
print(f"my_set_1: {red.smembers('my_set_1')}")
# Добавить элемент в set 2
red.sadd('my_set_2', 'X')
print(f"my_set_2: {red.smembers('my_set_2')}")
# Добавить элемент в set 2
red.sadd('my_set_2', 'Z')
print(f"my_set2: {red.smembers('my_set_2')}")
# Объединение set 1 и set 2
print(f"sunion: {red.sunion('my_set_1', 'my_set_2')}")
# Пересечение set 1 и set 2
print(f"sinter: {red.sinter('my_set_1', 'my_set_2')}")

print('-' * 20)
record = {
    "name": "Denis",
    "phone": "9115654848",
    "id": "11111"
}


print(red.hset('business', mapping=record))
print(f"business: {red.hgetall('business')}")

