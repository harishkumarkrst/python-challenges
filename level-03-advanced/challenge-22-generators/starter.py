def count_up(start, end):
    """
    Generator that yields numbers from start to end.
    """
    for i in range(start, end + 1):
        yield i


def fibonacci_generator():
    """
    Infinite Fibonacci generator.
    """
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def take(generator, n):
    """
    Return first n values from generator as a list.
    """
    return [next(generator) for _ in range(n)]


def squares_generator(limit):
    """
    Generator for perfect squares up to limit.
    """
    i = 1

    while i * i <= limit:
        yield i * i
        i += 1
