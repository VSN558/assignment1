# Problem 6: Flatten a list of lists

def flatten_list(list_of_lists):
    """
    Given a list of lists, returns a new list with all elements in a single level.

    Args:
    - list_of_lists (list): a list of lists

    Returns:
    - flattened_list (list): a new list with all elements in a single level
    """
    flattened_list = []
    for sublist in list_of_lists:
        for element in sublist:
            flattened_list.append(element)
    return flattened_list

list1 = ["Sriniekth", "vamsi", ["558"]]

print(flatten_list(list1))