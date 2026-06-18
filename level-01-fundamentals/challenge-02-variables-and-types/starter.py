def get_type_name(value):
    """
    TODO:
    Return the type name of the given value as a string.

    Examples:
        get_type_name(42)      should return "int"
        get_type_name(3.14)    should return "float"
        get_type_name("hello") should return "str"
        get_type_name(True)    should return "bool"

    Hint: Use type(value).__name__ to get the type name as a string.
    """
    return type(value).__name__


def is_integer(value):
    """
    TODO:
    Return True if the value is an integer (int type), False otherwise.

    Examples:
        is_integer(5)     should return True
        is_integer(5.0)   should return False  (5.0 is a float, not int)
        is_integer("5")   should return False  (it's a string)
        is_integer(True)  should return False  (treat bool as not int)

    Hint: Use isinstance(value, int) but watch out — bool is a subclass of int in Python!
    To exclude booleans: isinstance(value, int) and not isinstance(value, bool)
    """
    return isinstance(value, int) and not isinstance(value, bool)


def is_string(value):
    """ 
    TODO:
    Return True if the value is a string (str type), False otherwise.

    Examples:
        is_string("hello") should return True
        is_string("")      should return True  (empty string is still a string)
        is_string(123)     should return False
        is_string(True)    should return False

    Hint: Use isinstance(value, str)
    """
    return isinstance(value, str)


def convert_to_int(value):
    """
    TODO:
    Convert the given value to an integer and return it.

    Examples:
        convert_to_int("42")  should return 42   (the integer, not the string)
        convert_to_int(3.9)   should return 3    (truncates, does not round)
        convert_to_int("7")   should return 7

    Hint: Use the int() function: int("42") returns 42
    """
    return int(value)


def convert_to_string(value):
    """
    TODO:
    Convert the given value to a string and return it.

    Examples:
        convert_to_string(99)   should return "99"
        convert_to_string(3.14) should return "3.14"
        convert_to_string(True) should return "True"

    Hint: Use the str() function: str(99) returns "99"
    """
    return str(value)


def add_numbers(a, b):
    """
    
    TODO:
    Add two numbers together and return the result.

    Examples:
        add_numbers(3, 4)     should return 7
        add_numbers(1.5, 2.5) should return 4.0
        add_numbers(-1, 1)    should return 0

    Hint: Use the + operator.
    """
    return a + b
