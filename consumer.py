#!/usr/bin/env python
"""
Consumer implementation for interaction with the RabbitMQ docker image
* Pull message from the queue and display on screen
"""
import sys
import os
import pika

def callback(channel, method, properties, body):
    message = body.decode('utf8')
    print(f"[+] Recieved: {message}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare('next')

    #   Queue must exists before trying to consume
    channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)
    print('[*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Stopping consumer ...")
        try: 
            sys.exit(0)
        except SystemExit:
            os._exit(0)