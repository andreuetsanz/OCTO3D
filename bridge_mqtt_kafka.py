import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import json

# Configura Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Callback cuando recibes un mensaje de MQTT
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic
    print(f"[MQTT] {topic} → {payload}")

    # Publica en Kafka
    kafka_topic = 'octoprint-data'
    message = {
        'topic': topic,
        'payload': payload
    }
    producer.send(kafka_topic, message)

# Configura el cliente MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect('localhost', 1883, 60)
mqtt_client.subscribe('octoprint/#')

# Mantente escuchando
mqtt_client.loop_forever()
