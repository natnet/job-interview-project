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

# insert a new value to ex_collection
db.ex_collection.insert({ name: "Alice", age: 25 })

# find specific element on collection
db.ex_collection.find({ name: "Alice" })

# update element on collection
db.ex_collection.update({ name: "Alice" }, { $set: { age: 26 } })

# delete collection on collection
db.ex_collection.remove({ name: "Alice" })

# Show all documents in the 'events' collection
db.events.find().pretty()
db.ex_collection.find().pretty()
