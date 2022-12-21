from kafka import KafkaProducer

# Set up the configuration for the Kafka producer
config = {
    "bootstrap.servers": "localhost:9092",
    "key.serializer": "org.apache.kafka.common.serialization.StringSerializer",
    "value.serializer": "org.apache.kafka.common.serialization.StringSerializer"
}

# Create a new Kafka producer
producer = KafkaProducer(**config)

# Send a message to the "messages" topic
producer.send("messages", key="message-key", value="Hello, Kafka!")

# Close the producer
producer.close()
