def title_case(text):
    """
    Convert text to Title Case.
    """
    return text.title()


def count_vowels(text):
    """
    Count vowels in the text.
    """
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count


def remove_duplicates(text):
    """
    Remove consecutive duplicate characters.
    """
    result = ""

    for char in text:
        if result == "" or char != result[-1]:
            result += char

    return result


def truncate(text, max_length):
    """
    Shorten text if it exceeds max_length.
    """
    if len(text) > max_length:
        return text[:max_length - 3] + "..."

    return text


def is_anagram(word1, word2):
    """
    Check whether two words are anagrams.
    """
    clean1 = word1.lower().replace(" ", "")
    clean2 = word2.lower().replace(" ", "")

    return sorted(clean1) == sorted(clean2)