#!/usr/bin/env python3
""" Redis script that returns a random key """


import redis 
from uuid import uuid4
from functools import wraps
from typing import Any, Callable,  Optional, Union


def call_history(method: Callable) -> Callable:
    def wrapper(self, *args, **kwargs) -> Any:
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(input_key, str(args))
        
        output = method(self, *args, **kwargs)
        
        self._redis.rpush(output_key, output)
        
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ call count
    """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """ Wrapping called method
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def replay(fn: Callable) -> None:
    """Display the history of calls of a function."""
    input_key = f"{fn.__qualname__}:inputs"
    output_key = f"{fn.__qualname__}:outputs"
    
    inputs = fn.__self__._redis.lrange(input_key, 0, -1)
    outputs = fn.__self__._redis.lrange(output_key, 0, -1)

    print(f"{fn.__qualname__} was called {len(inputs)} times:")

    for input_val, output_val in zip(inputs, outputs):
        print(f"{fn.__qualname__}(*{input_val.decode()}) -> {output_val.decode()}")

class Cache:
    '''  '''

    def __init__(self) -> None:
        """  """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''  '''
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key

    
def get(self, key: str, fn: Optional[Callable] = None) -> Any:
    '''  '''
    client = self._redis
    value = client.get(key)

    if not value:
        return
    if fn is int:
        return self.get_int(value)
    if fn is str:
        return self.get_str(value)
    if callable(fn):
        return fn(value)
    return value


    def get_str(self, data: bytes) -> str:
        '''  '''
        return data.decode("UTF-8")
    

    def get_int(self, data: bytes) -> str:
        '''  '''
        return int(data)
    

def count_calls(method: Callable) -> Callable:
    """ call count
    """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """ Wrapping called method
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper