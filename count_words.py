def count_words(text) -> dictionary:
    """
    This funcction gets a text and print a dictionary of each word and its length.
    @param text: text
    @return: dictionary of the words in the text and their lengths
    """
    new_text = [word for word in text.split() if word.isalpha()]

    words_dictionary = {word: len(word) for word in new_text}
    return(words_dictionary)


if __name__ == "__main__":
    print (count_words("my head hurts, this is too long of a day"))
    
