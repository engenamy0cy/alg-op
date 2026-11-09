import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

print("Name:", r.get("shop:name"))

user1 = r.hgetall("user:1")
print("user data 1:", user1)

product1 = r.hgetall("product:1")
print("dtaa product 1:", product1)