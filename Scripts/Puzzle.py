#! Python 3
# You have a vector of N integers and there is an element that appears more than N/2 times.
# Find that element in linear time O(N) and constant space O(1).


import time
import random
import numpy

def random_vector(quantity):
    # Generate random integer that occurs more than N/2 times
    quantity_n_2_integer = random.randint(quantity/2, quantity)
    n_2_integer = random.randint(0, 10000)
    vector = [n_2_integer] * quantity_n_2_integer

    # Generate the rest of integers:
    for i in range(0, (quantity-quantity_n_2_integer)):
        temp_int = random.randint(0, 10000)
        while temp_int == n_2_integer:
            temp_int = random.randint(0, 10000)
        vector.append(temp_int)

    # Shuffle the vector
    random.shuffle(vector)
    return vector, n_2_integer

final_vector, n_2_integer = random_vector(1000)

start = time.time()

print(final_vector() == n_2_integer)

stop = time.time()

print("It took {} seconds".format(str(stop - start))