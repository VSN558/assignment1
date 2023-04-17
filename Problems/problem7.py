# Problem 7: Reverse words in a string

def reverse_words(string):
    """
    Given a string, returns a new string with the order of words reversed.

    Args:
    - string (str): a string

    Returns:
    - reversed_string (str): a new string with the order of words reversed
    """
    words = string.split()
    reversed_words = words[::-1]
    reversed_string = " ".join(reversed_words)
    return reversed_string


s1 = "sriniketh"
print(reverse_words(s1))