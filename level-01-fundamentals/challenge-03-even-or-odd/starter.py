def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0

def classify_number(number):
    if is_even(number):
        return "even"
    else:
        return "odd"

classify_number(2)