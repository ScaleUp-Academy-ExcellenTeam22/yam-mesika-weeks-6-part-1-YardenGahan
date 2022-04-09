"""
This program reads a sentence and returns a list of all the words length.
"""

def words_length(string):
    words = string.split()
    words_len = [len(word) for word in words]
    return words_len


print(words_length("Toto, I've a feeling we're not in Kansas anymore"))