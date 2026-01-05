# Data Distribution
from numpy import random
import numpy as np
# Notes ---->
# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0
rand_1d_array_probablity = random.choice([1 , 3 , 6 , 4] , p=[0.0 , 0.1 , 0.4 , 0.5] , size=(10))
print(" Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9. : \n" , rand_1d_array_probablity)
# Note :: The sum of all probability numbers should be 1.

# You can return arrays of any shape and size by specifying the shape
#  in the size parameter.
# it returns the 2-D 3x3 matrix
rand_2d_array_probability = random.choice([1 ,2 ,3  ,5 ] , p=[0.1 , 0.2 , 0.3 , 0.4] , size=(3 , 3))
print("generating 2-D array of 3x3 matrix using choice method with parameter size and p for probability : \n" ,rand_2d_array_probability)

# Random Permutations
# A permutation refers to an arrangement of elements.
#  e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# The NumPy Random module provides two methods for this: shuffle() and permutation().

# Shuffling Arrays
# Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
rand_1d_shuffling_array = np.array([1 , 2 ,3 ,4 ,5])
# The shuffle() method makes changes to the original array.
random.shuffle(rand_1d_shuffling_array)
print("Generating the Shuffling Arrays :\n" ,rand_1d_shuffling_array)

# generating Permutation of Array
# The permutation() method returns a re-arranged array
#  (and leaves the original array un-changed).
rand_1d_array_permutation = np.array([1 , 3 , 5 ,3 ,2])
print("generating Permutation of Array: \n" ,
       random.permutation(rand_1d_array_permutation))


