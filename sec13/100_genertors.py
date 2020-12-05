
# Generator function allows us to write a function 
# that can send back a value and then later resume to pick uo where it left off

# generate a sequence of value over time 

# yield statement

# generator function will automatically suspend and resume their execution and state around the last point of value generation 


# list(range(0,10))


def create_cube(n):
    result = []
    for x in range(n):
        result.append( x ** 3)
    return result 

print(create_cube(10))              # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]    # keep whole list in menory


for x in create_cube(10):
    print(x)
                                    # 0
                                    # 1
                                    # 8
                                    # 27
                                    # 64
                                    # 125
                                    # 216
                                    # 343
                                    # 512
                                    # 729


# ****************************************************************************************************
# generator way - memory efficient

def create_cube_gen(n):
    # no creating a list
    for y in range(n):
        yield y ** 3
    # no returning anything 


print(create_cube_gen(10))          # <generator object create_cube_gen at 0x7fa80436b580>  
                                    # point to an address in memory 
                                    
print(list(create_cube_gen(10)))    # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]





# generator way - memory efficient
# not store in list 
# use yield keyword
def fib_gen(n):
    a = 1 
    b = 1
    for i in range(n):
        yield a 
        a, b = b, a + b

print(list(fib_gen(10)))            # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



# normal/ tradition 
def fib(n):
    a = 1
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, b + a
    return result 

print(fib(10))                      # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# ****************************************************************************************************

def simple_gen():
    for x in range(3):
        yield x 

for number in simple_gen():
    print(number)
                                    # 0
                                    # 1
                                    # 2

g = simple_gen()
print(g)                            # <generator object simple_gen at 0x7fbbb5bccba0>

print(next(g))                      # 0
print(next(g))                      # 1
print(next(g))                      # 2

# print(next(g))                      # Traceback (most recent call last):
                                    # File "100_genertors.py", line 100, in <module>
                                    #     print(next(g))
                                    # StopIteration
# ****************************************************************************************************


s = "hello"

for letter in s:
    print(letter)
                                    # h
                                    # e
                                    # l
                                    # l
                                    # o


# print(next(s))                      # TypeError: 'str' object is not an iterator

iter_s = iter(s)
print(next(iter_s))                     # h
print(next(iter_s))                     # e
print(next(iter_s))                     # l
print(next(iter_s))                     # l
print(next(iter_s))                     # o
print(next(iter_s))                     # Traceback (most recent call last):
                                        # File "100_genertors.py", line 127, in <module>
                                        #     print(next(iter_s))
                                        # StopIteration


