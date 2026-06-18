def reverse_string(text):
    return text[::-1]


def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)
