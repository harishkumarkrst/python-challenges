def safe_divide(a, b):
    """
    Divide a by b and return the result.
    If b is zero, return None.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def safe_int_convert(value):
    """
    Convert value to integer.
    If conversion fails, return None.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def get_list_item(lst, index):
    """
    Return item at index.
    If index is invalid, return None.
    """
    try:
        return lst[index]
    except IndexError:
        return None


def validate_age(age):
    """
    Validate age between 0 and 150.
    Raise ValueError if invalid.
    """
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")
    return True
