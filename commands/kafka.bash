# Access the Kafka container with an interactive shell
docker exec -it job-interview-project-kafka-1 /bin/sh 

# Create a new Kafka topic named 'ex_topic'
kafka-topics --create --topic ex_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# List all Kafka topics
kafka-topics --list --bootstrap-server localhost:9092

# Consume messages from the 'EVENTS' topic from the beginning
kafka-console-consumer --topic ex_topic --bootstrap-server localhost:9092 --from-beginning

#delete events topic
kafka-topics --delete --topic EVENTS --bootstrap-server localhost:9092

#delete ex_topic topic
kafka-topics --delete --topic ex_topic --bootstrap-server localhost:9092

#produce message
kafka-console-producer --topic ex_topic --broker-list localhost:9092