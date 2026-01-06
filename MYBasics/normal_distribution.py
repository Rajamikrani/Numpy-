from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# generating a random normal distribution of 2x3 Matrix.
normal_rand_arr = random.normal(size = (2 , 3))
print("Random Normal Distribution Matrix : \n" ,normal_rand_arr)

# Generate a random normal distribution of size 2x3
#  with mean at 1 and standard deviation of 2:
normal_rand_dist = random.normal(loc = 1 , scale = 2 , size = (2 ,3))*10
print("Normal dist with mean and SD :\n" , normal_rand_dist)

# Visualization of Normal Distribution
sns.displot(random.normal(size=1000), kind="kde")
plt.show()

# Random Normal Distribution Matrix : 
#  [[-0.40524404 -1.09457719  0.32283379]
#  [ 2.23092399  0.30088172 -0.60241457]]

# Normal dist with mean and SD :
#  [[14.24445743 31.03429378  8.00638478]
#  [14.35486747 26.59458975 19.83665722]]