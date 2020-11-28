
# Tuples are similar to list 

# but tuple is IMMUTABLE - can NOT change/ re-assign

# tuples use () prenthesis


# count()
# index()


t = (1, 2, 3)
mylist = [1, 2, 3]

print(type(t))          # <class 'tuple'>
print(type(mylist))     # <class 'list'>


print(t[0])             # 1
print(t[-1])            # 3
print(mylist[0])        # 1
print(mylist[-1])       # 3


# count()
# index()
new_tuple_list = ("a", "a", "b", "a", "c")
print(new_tuple_list.count("a"))            # 3
print(new_tuple_list.index("b"))            # 2


