# Access the Kafka container with an interactive shell
docker exec -it job-interview-project-kafka-1 /bin/sh 

# List the contents of /usr/bin/ to locate Kafka CLI tools
ls /usr/bin/

# Create a new Kafka topic named 'ex_topic'
kafka-topics --create --topic ex_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# List all Kafka topics
kafka-topics --list --bootstrap-server localhost:9092

# Consume messages from the 'EVENTS' topic from the beginning
kafka-console-consumer --topic EVENTS --bootstrap-server localhost:9092 --from-beginning

