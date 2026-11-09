import json
import uuid

import pika
import redis

r = redis.Redis(
    host = 'localhost',
    port=6379,
    decode_response=True
)
order_id = str(uuid.uuid4())[:S]

order = {
    "id":order_id,
    "product":"iphon_18"                                                                                                                                                                                                   
}

#Подключиться к rabitMq
# создаем для подключения логин пароль

credentials = pika.PlainCredentials(
    "demo":"demo123"
)

channel = connections.channel()
# Создаем очередь
channel.queue_declare(
    queue = "order",
    durable = True,
    arguments = {"x-queue-type":"quorum"}
)

#Включаем подтверждение пуюликации 
channel.confirm_delivery()

#Отправка сообщения
channel.basic_publish(
    exchange="",
    routing_key = "orders",
    body = json.dumps(order), encode= ("utf-8"),
    properties= pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent,
        content_type="applications/json"
    ),
    mandatory = True
)

print(f"заказ вставлен в очередь {order_id}")

connections.close()

# Создается уникальный номер заказа
#Redis сохраняет товар и статус queued - ожидание обработки
# Python подключается к RabbitMq
# Создает очередь с именем orderds если ее еще нет
# Python отправляет сообщение с Id заказа и товара
#RabbitMq - принимает сообщение и помещяет его в очередь
# Другая программа worker забирает сообщение и выполняет задачу

# Ваш Код сам ничего не доставляет и не обрабатывает
# Он только создает заказ и отправляет сообщение
# connection - каналы - сетевое Tcp - соединение с RabbitMq
#channel - логический канал AMQP - внутри этого соединения

#pika.PlainCredentials - Создать реквезиты авторизации
#pika.ConnectiomParameters - задать параметры соединения
#pika.BlockingConnection - Подключиться к RabbitMq
#connection.channel() - Открыть AMQP - соединения
#queue.declare() - обьявить очередь
# confirm_delivery() - включить подтверждение публикации
# basic_publish() - Опубликовать сообщение
# pika.BasicProperties() - Задать свойства сообщения
# start_consuming() - Запустить полученное сообщение
# basic_qos() - ограничить код неподтвержденных сообщений
# basic_ack() - подтвердить обратотку
# basic_nack() - отрицательно подвердить обработку
# basic_get() - получить олно сообщение без постоянной подписки
# queue_purge() - очистка ожидания сообщения очереди
# queue_delete() - удалить очередь
# connection.close() - закрыть соединение

#Отправитель sender.py не обязан знать кто именно будет выполнять заказ
# Он передает сообщение в RabbitMq в отдельном worker забирает задачу
# тогда когда готов ее выполнить 
# именно на этом строится принцип всех микросервисов фоновых задач очереди 
# обработки изображение почтовые рассылки
# и другие backend структуры