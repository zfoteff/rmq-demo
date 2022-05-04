#!/usr/bin/env python
"""
Producer implementation for interaction with the RabbitMQ docker image
* Publish message directly to queue
"""

import pika
import sys

message = ''.join(sys.argv[1:]) or "Hello, world!"
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange="",
                      routing_key='hello',
                      body=message)

print("[x] Sent message to the queue")
connection.close()