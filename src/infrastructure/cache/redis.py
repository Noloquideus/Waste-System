from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import redis.asyncio as redis
from redis.asyncio.connection import ConnectionPool
from src.config import CONFIG


async def init_redis():
    pool = ConnectionPool.from_url(url=f'redis://{CONFIG.REDIS_HOST}:{CONFIG.REDIS_PORT}')
    r = redis.Redis(connection_pool=pool)
    FastAPICache.init(RedisBackend(r), prefix='cache')
    