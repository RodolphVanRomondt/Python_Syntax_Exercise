def print_upper_words(words, must_start_with=["h", "y"]):
    """ print each word of the first list in uppercase and on a separate line
        if it starts with the letter of the second list
    """

    for word in words:
        for cha in must_start_with:
            if word.upper().startswith(cha.upper()):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["g"])
