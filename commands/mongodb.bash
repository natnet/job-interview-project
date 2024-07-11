

# Connect to the MongoDB container and start a bash session
docker exec -it mongodb /bin/bash

# Inside the MongoDB container, start the MongoDB Shell (mongosh)
mongosh

# Use the 'test' database
# Switch to the 'test' database (note: this will not create it until data is added)
use test

# Drop the 'test' database
db.dropDatabase()

# Create a new collection named 'ex_collection'
db.createCollection("ex_collection")

# Show all documents in the 'events' collection
db.events.find().pretty()
