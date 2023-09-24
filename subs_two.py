import pika
import _MQPARAMS as mq

def on_mess(channel, method_frame, header_frame, body):
    if body == 'procedure':
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    else:
        print(f'body is not procedure, body is {type(body)}')


creds = pika.credentials.PlainCredentials(mq.user, mq.userpass)
connection = pika.BlockingConnection(pika.ConnectionParameters(mq.server, mq.port, 'main', creds))
channel = connection.channel()

channel.basic_consume('dev1', on_mess)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
except Exception:
    channel.stop_consuming()

print('DONE')
