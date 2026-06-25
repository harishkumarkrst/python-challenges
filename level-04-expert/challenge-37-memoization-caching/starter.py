import functools
import time


def memoize(func):
    """
    Decorator that caches function results.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)

        return cache[args]

    wrapper.cache = cache
    return wrapper


def fibonacci_naive(n):
    """
    Naive recursive Fibonacci.
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


@functools.lru_cache(maxsize=None)
def fibonacci_cached(n):
    """
    Cached Fibonacci using lru_cache.
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


class Cache:
    """
    Simple cache with max size and oldest eviction.
    """

    def __init__(self, max_size=128):
        self.max_size = max_size
        self._store = {}
        self._order = []


    def get(self, key):
        """
        Return value or None.
        """
        return self._store.get(key, None)


    def set(self, key, value):
        """
        Add or update cache value.
        """
        if key in self._store:
            self._store[key] = value
            return

        if len(self._order) >= self.max_size:
            oldest = self._order.pop(0)
            del self._store[oldest]

        self._store[key] = value
        self._order.append(key)


    def delete(self, key):
        """
        Remove key.
        """
        if key in self._store:
            del self._store[key]
            self._order.remove(key)


    def clear(self):
        """
        Empty cache.
        """
        self._store.clear()
        self._order.clear()


    def size(self):
        """
        Return cache size.
        """
        return len(self._store)