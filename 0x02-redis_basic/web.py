#!/usr/bin/env python3
'''  '''
import redis
import requests
from functools import wraps

redis_client = redis.Redis()


def cache_page(func):
    """Decorator to cache the page content."""
    @wraps(func)
    def wrapper(url: str) -> str:
        cached_content = redis_client.get(url)
        
        if cached_content:
            redis_client.incr(f"count:{url}")
            return cached_content.decode('utf-8')
        
        content = func(url)
