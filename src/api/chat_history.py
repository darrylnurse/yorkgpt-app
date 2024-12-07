from langchain_redis import RedisChatMessageHistory
import redis

REDIS_URL = "redis://historydb:6379"

client = redis.Redis(host='historydb', port=6379, db=0)

try:
    pong = client.ping()
    if pong:
        print("Connected to Redis!")
except redis.ConnectionError:
        print("Could not connect to Redis.")

def get_chat_history (session_id: str):
    return RedisChatMessageHistory(session_id=session_id, redis_url=REDIS_URL)

