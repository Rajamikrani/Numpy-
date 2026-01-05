from numpy import random

# generating random integer number from 0 to 10.
randInt = random.randint(10)
print("generating random integer number : " , randInt)

#  generating random number value from 0 to 1
randNum = random.rand()
print("generating random number value from 0 to 1 : " , randNum)

# generate the random array
# size declare the length of array.
randArray = random.randint(100 , size=5) 
print("generating random array : " , randArray)

# generate a 2-D array 
rand2DArray = random.randint(10 , size = (3 , 3))
print("generating random 2-D array : \n" , rand2DArray)

# like 2-d we also generate 3-d 
rand3DArray = random.randint(10 , size = (3 , 3 , 3))
print("generating random 3-D array : \n" , rand3DArray)

# Generate Random Number From Array
# Note --->
# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.
randChoice = random.choice([1 ,3 ,5 ,2])
print("Return one of the values in an array : " , randChoice)
# Note --->
# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.
# Generate a 2-D array that consists of the values
#  in the array parameter (3, 5, 7, and 9):

x = random.choice([1 ,3 , 7] , size= (3 , 4))
print("random 2-d array : \n" , x)

# Output ======>>>
# generating random integer number :  6
# generating random number value from 0 to 1 :  0.9401757891588691
# generating random array :  [23 79 19 71 14]
# generating random 2-D array : 
#  [[0 0 8]
#  [2 9 4]
#  [2 1 2]]
# generating random 3-D array :
#  [[[7 7 4]
#   [6 0 2]
#   [0 4 0]]

#  [[8 0 1]
#   [4 5 5]
#   [7 6 5]]

#  [[9 8 4]
#   [6 9 8]
#   [6 5 7]]]
# Return one of the values in an array :  2
# random 2-d array :
#  [[1 1 3 1]
#  [7 1 3 7]
#  [7 7 3 7]]