def count_words(text):
    """
    Count how many times each word appears in the text.
    """
    words = text.lower().split()

    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def most_common_word(text):
    """
    Return the word that appears most often in the text.
    """
    counts = count_words(text)

    if counts == {}:
        return None

    return max(counts, key=counts.get)


def unique_words(text):
    """
    Return a sorted list of all unique words.
    """
    words = text.lower().split()

    return sorted(set(words))