import pika, json

params = pika.URLParameters('amqps://ninsszay:ovu7hbui43AMKRy4ZL_LYz-WsBN-5vbV@lionfish.rmq.cloudamqp.com/ninsszay')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()

