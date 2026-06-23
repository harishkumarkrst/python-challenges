from functools import reduce


def apply_to_all(func, items):
    """
    Apply func to every item in the items list and return results.
    """
    return list(map(func, items))


def keep_if(func, items):
    """
    Return items for which func returns True.
    """
    return list(filter(func, items))


def reduce_list(func, items, initial):
    """
    Combine all items into a single value using reduce.
    """
    return reduce(func, items, initial)


def pipeline(value, *funcs):
    """
    Apply each function one by one to the value.
    """
    result = value

    for func in funcs:
        result = func(result)

    return result


def compose(f, g):
    """
    Return a function that applies g first, then f.
    """
    return lambda x: f(g(x))