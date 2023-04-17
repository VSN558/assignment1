#Problem 1: Find the sum of all even numbers in a list

def sum_even_numbers(numbers):
    """
    Given a list of numbers, returns the sum of all even numbers in the list.

    Args:
    - numbers (list): a list of numbers

    Returns:
    - sum_of_evens (int): the sum of all even numbers in the list
    """
    sum_of_evens = 0
    for number in numbers:
        if number % 2 == 0:
            sum_of_evens += number
    return sum_of_evens


list1 = [2,3,4,56,6,78,]

print (sum_even_numbers(list1))