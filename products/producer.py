import pika, json

params = pika.URLParameters('amqps://ninsszay:ovu7hbui43AMKRy4ZL_LYz-WsBN-5vbV@lionfish.rmq.cloudamqp.com/ninsszay')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
