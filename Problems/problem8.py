# Problem 8: Implement a binary search algorithm

def binary_search(numbers, target):
    """
    Searches for the target value in a sorted list of numbers using binary search.

    Args:
    - numbers (list): a sorted list of numbers
    - target (int): the target value to search for

    Returns:
    - index (int): the index of the target value, or -1 if not found
    """
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

list1 = [1,2,4,6,7,9,12,13,15]
print(binary_search(list1,4))
