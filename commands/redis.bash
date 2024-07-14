docker exec -it redis redis-cli


# List all keys
KEYS *

#set key value
SET mykey "Hello, Redis!"

# Retrieve the value of a string key
GET "mykey"

# delete key value
DEL mykey

# Clear all
FLUSHALL
