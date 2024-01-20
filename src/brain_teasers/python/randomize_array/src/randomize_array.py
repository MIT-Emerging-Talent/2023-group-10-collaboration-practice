import random

def randomize_array(original_array):
    randomized_array = original_array.copy()

    random.shuffle(randomized_array)
    return (randomized_array)
