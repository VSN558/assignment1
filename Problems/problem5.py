#Problem 5: Remove duplicates from a list

def remove_duplicates(elements):
    """
    Given a list of elements, returns a new list with duplicates removed.

    Args:
    - elements (list): a list of elements

    Returns:
    - unique_elements (list): a new list with duplicates removed
    """
    unique_elements = []
    for element in elements:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements


list1 = ["sriniketh", "vamsi", 558, "sriniketh"]
print(remove_duplicates(list1))