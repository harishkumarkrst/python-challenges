def clean_string(text):
    return text.lower().replace(" ", "")


def is_palindrome(text):
    cleaned = clean_string(text)
    return cleaned == cleaned[::-1]

