# Problem 4: Count the number of occurrences of each word in a string

def word_count(sentence):
    """
    Given a sentence, returns a dictionary containing the number of occurrences of each word in the sentence.

    Args:
    - sentence (str): a string containing the sentence

    Returns:
    - word_dict (dict): a dictionary containing the number of occurrences of each word in the sentence
    """
    # Convert the sentence to lowercase and split it into words
    words = sentence.lower().split()
    # Initialize an empty dictionary to store the word counts
    word_dict = {}
    # Iterate over each word in the sentence
    for word in words:
        # If the word is not already in the dictionary, add it with a count of 1
        if word not in word_dict:
            word_dict[word] = 1
        # If the word is already in the dictionary, increment its count
        else:
            word_dict[word] += 1
    return word_dict


s1 = """The sunblock was handed to the girl before practice, but the burned skin was proof she did not apply it.
She borrowed the book from him many years ago and hasn't yet returned it.
She only paints with bold colors; she does not like pastels."""

print(word_count(s1))
