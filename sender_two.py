import pika

creds = pika.credentials.PlainCredentials('admin', 'keepwalking123#')

connection = pika.BlockingConnection(pika.ConnectionParameters('82.146.57.126', '5672', 'main', creds))
channel = connection.channel()

channel.queue_declare('dev1', durable=True, auto_delete=False)
channel.queue_bind(queue='dev1', exchange='amq.direct', routing_key='dev1')

for x in range(1, 1100000):
    channel.basic_publish(exchange='amq.direct',
                          routing_key='dev1',
                          body=f'Producer 2')
    # print(f" [x] Sent 'Hello World! {x}'")

connection.close()
print('DONE')
