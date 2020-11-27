

# char :          h   e   l   l   o
# index:          0   1   2   3   4
# reverse index:  0   -4  -3  -2  -1


my_string = "hello world"

print(my_string)        # hello world

print(my_string[0])     # h
print(my_string[8])     # r
print(my_string[-1])    # d



mystring = "abcdefghijk"
print(mystring[2:])         # cdefghijk

# up to but not include stop index
# [start:stop:step]
print(mystring[0:3])        # abc
print(mystring[3:6])        # def

print(mystring[::])         # abcdefghijk
print(mystring[::2])        # acegik

# reverse
print(mystring[::-1])       # kjihgfedcba







