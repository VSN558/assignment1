# Problem 2: Check if a string is a palindrome

def is_palindrome(word):
    """
    Given a word, returns True if it is a palindrome, False otherwise.

    Args:
    - word (str): a string

    Returns:
    - is_palindrome (bool): True if word is a palindrome, False otherwise
    """
    # Convert the word to lowercase and remove non-alphanumeric characters
    word = "".join(char.lower() for char in word if char.isalnum())
    # Check if the word is equal to its reverse
    return word == word[::-1]


s1 = "12321"
print (is_palindrome(s1))