
import math

# help(math)
# print(help(math))

value = 4.5 

print(math.floor(value))        # 4
print(math.ceil(value))         # 5
print(round(5.5))               # 6


print(math.pi)                  # 3.141592653589793
# ****************************************************************
from math import pi
print(pi)                       # 3.141592653589793
# ****************************************************************

print(math.e)                   # 2.718281828459045
print(math.log(math.e))         # 1.0
print(math.log(100, 10))        # 2.0
print(math.log(8, 2))           # 3.0

print(math.inf)                 # inf
print(math.nan)                 # nan


print(math.sin(10))             # -0.5440211108893699
print(math.cos(90))             # -0.4480736161291701

print(math.degrees(pi))         # 180
print(math.radians(180))        # 3.141592653589793

# *********************************************************************************

import random

# randint(a, b) - random int in range [a, b], including both point
print(random.randint(0, 100))


my_list = list(range(0, 20))
print(my_list)                  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(random.choice(my_list))   # 


# sample wit hreplacement - choices() - with repeat
print(random.choices(population=my_list, k=5))          # [5, 4, 8, 14, 8]  will pick from population, and as much as k elements 


# sample without replacemnet - sample() - no repeat
print(random.sample(population=my_list, k=5))           # [19, 10, 5, 16, 17]

# can NOT store into a variable
random.shuffle(my_list)
print(my_list)          # [18, 11, 15, 17, 19, 13, 1, 12, 5, 14, 4, 8, 7, 16, 6, 2, 3, 0, 9, 10]

# equal opportunity of chosen 
print(random.uniform(a=0.0, b=20.0))            # 16.36365687557594


# Numpy for ML





