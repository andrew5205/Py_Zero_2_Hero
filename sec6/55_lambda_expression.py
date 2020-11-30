
# Lambda expression
# Map, filter


def squar(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5, 6]

map(squar, my_nums)
print(map(squar, my_nums))          # <map object at 0x7fc353ac8790>

for item in map(squar, my_nums):
    print(item)
                    # 1
                    # 4
                    # 9
                    # 16
                    # 25
                    # 36

print(map(squar, my_nums))                  # <map object at 0x7fab765c8790>

# convert to list 
list(map(squar, my_nums))
# print(list(map(squar, my_nums)))        # [1, 4, 9, 16, 25, 36]



# ******************************************************************************

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "even"
    else:
        return mystring[0]

myString = ["Andy", "Sally", "Eve"]
print(splicer(myString))                # Andy
# convert to list 
list(map(splicer, myString))
print(list(map(splicer, myString)))     # ['even', 'S', 'E']

# hint 
# while using map, just pass the function as arguement, NOT function 
# map will execute it anyway

# print(list(map(splicer(), myString)))

# Traceback (most recent call last):
#   File "55_lambda_expression.py", line 46, in <module>
#     print(list(map(splicer(), myString)))
# TypeError: splicer() missing 1 required positional argument: 'mystring'




# ******************************************************************************
# filter() 
# can only through Treu/ False 

def check_even(num):
    return num % 2 == 0

my_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter(check_even, my_num)
print(filter(check_even, my_num))           # <filter object at 0x7f81d0abe790>

# convert to list 
list(filter(check_even, my_num))
print(list(filter(check_even, my_num)))     # [2, 4, 6, 8, 10]

for n in filter(check_even, my_num):
    print(n)
                # 2
                # 4
                # 6
                # 8
                # 10


# ******************************************************************************
# lambda - is an Anonymous function

def square(num):
    result = num ** 2
    return result 

print(square(3))        # 9

# will equal to above 
# lambda arug: (what to return)
lambda num: num ** 2 

s = lambda num: num ** 2 
print(s(3))             # lambda num: num ** 2 
# ******************************************************************************



print(list(map(lambda num: num ** 2, my_nums)))             # [1, 4, 9, 16, 25, 36]

print(list(filter(lambda num: num % 2 == 0, my_num)))       # [2, 4, 6, 8, 10]

print(list(map(lambda x: x[0], myString)))                  # ['A', 'S', 'E']