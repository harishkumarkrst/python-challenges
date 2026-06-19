import math


def is_prime(n):
    """
    Return True if n is a prime number, False otherwise.
    """

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def get_primes(limit):
    """
    Return a list of all prime numbers from 2 up to and including limit.
    """

    primes = []

    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)

    return primes