def double_numbers(numbers):
    """
    Return a new list where each number is doubled.
    """
    return [x * 2 for x in numbers]


def filter_evens(numbers):
    """
    Return a new list containing only even numbers.
    """
    return [x for x in numbers if x % 2 == 0]


def squares(numbers):
    """
    Return a new list where each number is squared.
    """
    return [x ** 2 for x in numbers]


def filter_long_words(words, min_length):
    """
    Return words with length >= min_length.
    """
    return [word for word in words if len(word) >= min_length]


def uppercase_words(words):
    """
    Return words converted to uppercase.
    """
    return [word.upper() for word in words]