"""
This program gets a text and print a dictionary of each word and its length.
"""


def count_words(text):
    new_text = [word for word in text.split() if word.isalpha()]

    words_dictionary = {word: len(word) for word in new_text}
    print(words_dictionary)
