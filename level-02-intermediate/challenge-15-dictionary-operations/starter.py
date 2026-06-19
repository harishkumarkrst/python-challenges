def get_value(d, key, default=None):
    """
    Return value for key, or default if key doesn't exist.
    """
    return d.get(key, default)


def add_or_update(d, key, value):
    """
    Add new key or update existing key.
    """
    d[key] = value
    return d


def remove_key(d, key):
    """
    Remove key if it exists.
    """
    if key in d:
        del d[key]

    return d


def merge_dicts(d1, d2):
    """
    Merge two dictionaries into a new dictionary.
    """
    result = d1.copy()
    result.update(d2)

    return result


def invert_dict(d):
    """
    Swap keys and values.
    """
    return {v: k for k, v in d.items()}


def get_all_keys(d):
    """
    Return sorted list of keys.
    """
    return sorted(d.keys())