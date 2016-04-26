def break_words(stuff):
    """This function will break up words for us. """
    words = stuff.split(' ')
    return words
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print (word)
def print_last_word(words):
    """prints the last word after popping it off."""
    word = words.pop(-1)
    print (word)
    
