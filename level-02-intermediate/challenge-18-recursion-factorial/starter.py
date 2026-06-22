def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    """
    # Base case
    if n <= 1:
        return 1

    # Recursive case
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """
    Calculate factorial using loop.
    """
    result = 1

    for i in range(2, n + 1):
        result = result * i

    return result


def count_down(n):
    """
    Return list counting down from n to 1 using recursion.
    """
    # Base case
    if n <= 0:
        return []

    # Recursive case
    return [n] + count_down(n - 1)