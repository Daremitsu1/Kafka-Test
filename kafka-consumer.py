from kafka import KafkaConsumer

# Set up the configuration for the Kafka consumer
config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "my-group",
    "key.deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
    "value.deserializer": "org.apache.kafka.common.serialization.StringDeserializer"
}

# Create a new Kafka consumer
consumer = KafkaConsumer("messages", **config)

# Consume messages from the "messages" topic
for message in consumer:
    print(message.key, message.value)

# Close the consumer
consumer.close()
