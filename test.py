import redis

# יצירת חיבור לרדיס
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# פונקציה לשליפת כל המפתחות והערכים
def read_all_values(r):
    cursor = '0'  # נקודת התחלה לסריקה
    all_keys = []
    all_values = {}
    
    while cursor != 0:
        cursor, keys = r.scan(cursor=cursor, count=100)
        all_keys.extend(keys)
    
    for key in all_keys:
        all_values[key] = r.get(key)
    
    return all_values

# קריאת כל המפתחות והערכים
all_data = read_all_values(r)

# הדפסת כל המפתחות והערכים
for key, value in all_data.items():
    print(f"Key: {key}, Value: {value}")
