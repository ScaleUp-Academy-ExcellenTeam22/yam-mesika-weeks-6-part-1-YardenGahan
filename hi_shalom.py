def words_length(string) ->list :
    """
    This function reads a sentence and returns a list of all the words length.
    @param string: a sentence
    @return: list of words length
    """
    return [len(word) for word in string.split()]


if __name__ == "__main__":
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
    
