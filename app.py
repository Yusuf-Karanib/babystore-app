from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (SSL is mandatory for Serverless)
cache = redis.Redis(
    host='yusuf-cache-wgmhtm.serverless.use1.cache.amazonaws.com',
    port=6379,
    decode_responses=True,
    ssl=True
)

@app.route('/')
def home():
    try:
        # Look for the message in the cache
        val = cache.get('week7_status')
        if val:
            return f"{val} (Cache Hit)"
        
        # If not found, save it to cache for 1 hour
        msg = "Babystore App Build: week7-final"
        cache.setex('week7_status', 3600, msg)
        return f"{msg} (Cache Miss)"
        
    except Exception:
        # Fallback if the cache is unreachable
        return "Babystore App Build: week7-final (Cache Offline)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)