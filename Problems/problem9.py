# Problem 2: Implement a quicksort algorithm

def quicksort(numbers):
    """
    Sorts a list of numbers in ascending order using quicksort.

    Args:
    - numbers (list): a list of numbers

    Returns:
    - sorted_numbers (list): a new list with the numbers sorted in ascending order
    """
    if len(numbers) < 2:
        return numbers

    pivot = numbers[0]
    less = [num for num in numbers[1:] if num <= pivot]
    greater = [num for num in numbers[1:] if num > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

list1 = [3,56,3,2,9,10,11,23]
print(quicksort(list1))