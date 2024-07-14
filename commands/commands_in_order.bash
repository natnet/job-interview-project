# prestart 
docker-compose create

# Step i: Start Kafka and zookeeper
docker start job-interview-project-zookeeper-1
docker start job-interview-project-kafka-1

# Step ii: Create a topic in Kafka
docker exec -it job-interview-project-kafka-1 /bin/sh 
kafka-topics --create --topic ex_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Step iii: Run the producer
docker start job-interview-project-producer-1

# Step iv: Verify data in the topic using Kafka CLI
docker exec -it job-interview-project-kafka-1 /bin/sh 
kafka-console-consumer --topic EVENTS --bootstrap-server localhost:9092 --from-beginning

# Step v: Start MongoDB container
docker start mongodb

# Step vi: Create a collection in MongoDB
docker exec -it mongodb /bin/bash
mongosh
db.createCollection("ex_collection")

# Step vii: Run the consumer
docker start job-interview-project-consumer-1

# Step viii: Show data in MongoDB
docker exec -it mongodb /bin/bash
mongosh
use test
db.events.find().pretty()


# Step ix: Start Redis container
docker start redis


# Step x: Run ETL
docker start job-interview-project-mongotoredis-1


# Step xi: Show data in Redis
docker exec -it redis redis-cli
KEYS *

# Step xii: Stop ETL process
docker stop job-interview-project-mongotoredis-1


# Step xiii: Run ETL process again
docker start job-interview-project-mongotoredis-1


# Step xiv: Show that ETL continues processing from the last processed point
docker exec -it redis redis-cli
KEYS *
