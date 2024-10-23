#!/usr/bin/env python3
""" Redis script that returns a random key """
#from redis import Redis, redis
'''
import redis
import random
import uuid
from typing import Union


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
'''

import redis 
from uuid import uuid4
from functools import wraps
from typing import Any, Callable,  Optional, Union

class Cache:
    '''  '''

    def __init__(self) -> None:
        """  """
        self._redis = redis.Redis()
        self._redis.flushdb()

    #@call_history
    #@count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''  '''
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key

    
    
