import pika


def on_mess(channel, method_frame, header_frame, body):
    if body.decode("utf-8") == 'procedure':
        print('Процедура взята в очередь')
    else:
        print(f'body is not procedure, body is {type(body)}')
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)  # можно вручную присвоить данному сообщению статус Acked


creds = pika.credentials.PlainCredentials('admin', 'keepwalking123#')
connection = pika.BlockingConnection(pika.ConnectionParameters('82.146.57.126', '5672', 'main', creds))
channel = connection.channel()

channel.basic_consume('dev1', on_mess, auto_ack=True)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
except Exception:
    channel.stop_consuming()

print('DONE')
