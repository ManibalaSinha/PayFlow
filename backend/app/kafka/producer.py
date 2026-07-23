from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError
import json

producer = None

def get_producer():
    global producer
    if producer is None:
        producer = KafkaProducer(
            bootstrap_servers=["localhost:9092"],
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        )
    return producer

def publish_event(topic, event):
    try:
        p = get_producer()
        p.send(topic, event)
        p.flush()
    except KafkaTimeoutError:
        print("Kafka unavailable; event not published.")