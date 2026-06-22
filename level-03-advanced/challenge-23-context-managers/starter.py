import time
from contextlib import contextmanager


class Timer:
    """
    Context manager for measuring execution time.
    """

    def __init__(self):
        self.elapsed = 0
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        self.elapsed = end - self.start

        return False


@contextmanager
def managed_list():
    """
    Generator-based context manager.
    """
    items = []

    yield items


class suppress_errors:
    """
    Context manager that suppresses selected exceptions.
    """

    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exception_types):
            return True

        return False