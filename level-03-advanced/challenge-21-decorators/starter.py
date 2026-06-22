import functools
import time


def timer(func):
    """
    Decorator that measures execution time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        elapsed = end - start

        print(f"{func.__name__} took {elapsed:.2f} seconds")

        return result

    return wrapper


def logger(func):
    """
    Decorator that logs function calls and results.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")

        return result

    return wrapper


def validate_positive(func):
    """
    Decorator that checks all arguments are positive.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                raise ValueError("All arguments must be positive")

        return func(*args, **kwargs)

    return wrapper
