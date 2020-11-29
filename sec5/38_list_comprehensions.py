
# ******************************************************************
# using for loop
myString = "hello"

myList = []

for letter in myString:
    myList.append(letter)

print(myList)                                       # ['h', 'e', 'l', 'l', 'o']

# ******************************************************************
# efficient way in python

my_efficient_list = [letter for letter in myString]
print(my_efficient_list)                            # ['h', 'e', 'l', 'l', 'o']

# hint
# default in append()
# new_list = [ append(e) (for e in range) (condition)]

my_num_list = [num for num in range(10)]
print(my_num_list)                                  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_sqr_list = [num ** 2 for num in range(10)]
print(my_sqr_list)                                  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


my_odd_list = [num for num in range(0,10) if num % 2 != 0]
print(my_odd_list)                                  # [1, 3, 5, 7, 9]


# C to F
celius = [0, 10, 24, 35.5]
fahrenheit = [ ( (9/5)*temp + 32) for temp in celius ]
print(fahrenheit)                                   # [32.0, 50.0, 75.2, 95.9]




# ******************************************************************
# if else in comprehension ( hard to read)
# hint tenary operator 

# new_list = [append(e) (tenary if/ else) (for e in range) ]
result = [ x if x%2 == 0 else "odd" for x in range(10)]
print(result)                                       # [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']


# ******************************************************************
# nested loop 

nested_list = []

for x in [1, 2, 3]:
    for y in [1, 10, 100]:
        nested_list.append(x * y)
print(nested_list)                  # [1, 10, 100, 2, 20, 200, 3, 30, 300]


# comprehension way
# new_list = [appedn(e) (for loop) (2nd for loop) ]
nested_list_comp = [ (x * y) for x in [1, 2, 3] for y in [1, 10, 100]]
print(nested_list)                  # [1, 10, 100, 2, 20, 200, 3, 30, 300]






