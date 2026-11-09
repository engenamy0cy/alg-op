import json
import time
import pika
import redis

r = redis.Redis(
    host="localhost",
    port="6379",
    decode_responses = True,
)

credentials = pika.PlainCredentials(
    "demo","demo123"
)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host= "localhost",
        credentials=credentials
    )
)

channel = connection.channel()

channel.queue_declare(
    queue="orders",
    durable=True,
    arguments={"x-queue-type":"quorum"}
)

#По одной задаче на обработчик
channel.basic_qos(prefetch_count=1)

def process_order(ch,method,properties,body):
    order = json.load(body.decode("utf-8"))
    order_id = order["id"]

    print(f"Получен заказ {order_id}")

    r.hset(
        f"order:{order_id}",
        "status",
        "processing"
    )

    #Имитирует обработку
    time.sleep(10)

    r.hset(
        f"order:{order_id}",
        "status",
        "done"
    )

    print(f"заказ выполнен {order_id}")

    ch.basik_ack(
        delivery_tag = method.delivery_tag
    )

channel.basik_consume(
    queue="orders",
    on_message_callback = process_order
)

print("Worker Ожидает заказы")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
finally:
    connection.close()