def fibonacci(n):
    """
    Return the nth Fibonacci number (0-indexed).
    """

    if n == 0:
        return 0

    if n == 1:
        return 1

    a, b = 0, 1

    for _ in range(n - 1):
        a, b = b, a + b

    return b


def fibonacci_sequence(count):
    """
    Return a list containing the first 'count' Fibonacci numbers.
    """

    if count == 0:
        return []

    sequence = []

    a, b = 0, 1

    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b

    return sequence