import pika
import _MQPARAMS as mq

creds = pika.credentials.PlainCredentials(mq.user, mq.userpass)

connection = pika.BlockingConnection(pika.ConnectionParameters(mq.server, mq.port, 'main', creds))
channel = connection.channel()

channel.queue_declare('dev1', durable=True, auto_delete=False)
channel.queue_bind(queue='dev1', exchange='amq.direct', routing_key='dev1')

for x in range(1, 5):
    channel.basic_publish(exchange='amq.direct',
                          routing_key='dev1',
                          body=f'Producer 1')
    # print(f" [x] Sent 'Hello World! {x}'")

connection.close()
print('DONE')