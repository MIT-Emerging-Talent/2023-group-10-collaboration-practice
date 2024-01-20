import random

def randomize_array(original_array):
    """
    The randomize_array function takes an input array, copies it and shuffle the elements inside
    to create a randomized copy of our original array
    
    Parameters:
    - original_array: The array to be randomized.

    Returns: A new list containing the elements of the original array in a random order.

    """

    randomized_array = original_array.copy()

    random.shuffle(randomized_array)
    return (randomized_array)
