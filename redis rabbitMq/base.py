import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.set("shop:name", "Super govnoShop")
r.set("shop:visits", "0")

r.hset("user:1", mapping={"name": "kepeer of the light", "lvl": 18, "role": "midle"})
r.hset("user:2", mapping={"name": "luna", "lvl": 16, "role": "carry"})

r.hset("product:1", mapping={"title": "ethereal blade", "price": 5200, "stock": 228})
r.hset("product:2", mapping={"title": "butterfly", "price": 5450, "stock": 666})

print("База данных успешно заполнена!")