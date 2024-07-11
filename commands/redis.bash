docker exec -it redis redis-cli

# Inside the Redis CLI

# List all keys
KEYS *

# Retrieve the value of a string key
GET "string_key"

# Clear all
FLUSHALL
