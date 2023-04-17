# Problem 3: Find the largest and smallest numbers in a list

def find_min_max(numbers):
    """
    Given a list of numbers, returns a tuple containing the minimum and maximum numbers in the list.

    Args:
    - numbers (list): a list of numbers

    Returns:
    - min_max (tuple): a tuple containing the minimum and maximum numbers in the list
    """
    min_num = float('inf')
    max_num = float('-inf')
    for number in numbers:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number
    min_max = (min_num, max_num)
    return min_max

list1 = [2,4,5,120,0,-12]
print (find_min_max(list1))
