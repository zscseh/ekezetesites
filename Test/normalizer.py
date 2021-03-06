def ispunct(c):
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for char in punctuations:
        if (c == char):
            return True
    return False


def isalpha(c):
    hun_alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in hun_alphabet:
        if (c == char):
            return True
    return False

# reduces the number of different characters to 30
def normalize_character(c):
    if (c.isspace()):
        return ' '
    if (c.isdigit()):
        return '0'
    if (ispunct(c)):
        return '_'
    if (isalpha(c)):
        return c
    return '*'


def normalize_text(text):
    normalized = ""
    for c in text:
        normalized += normalize_character(c)
    return normalized