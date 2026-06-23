import re


def is_valid_email(email):
    """
    Return True if email matches valid format.
    """
    pattern = r'^[\w.+-]+@[\w-]+\.[\w.]+$'
    return re.match(pattern, email) is not None


def extract_numbers(text):
    """
    Return all numbers found in text.
    """
    return re.findall(r'\d+', text)


def is_valid_phone(phone):
    """
    Validate phone format: +XX-XXX-XXX-XXXX
    """
    pattern = r'^\+\d{2}-\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone) is not None


def replace_whitespace(text):
    """
    Replace multiple spaces/tabs with single space.
    """
    return re.sub(r'[ \t]+', ' ', text)


def extract_hashtags(text):
    """
    Return all hashtags in text.
    """
    return re.findall(r'#\w+', text)