
# - append()
# - pop()
# -sort()
# -reverse()


my_list = [1, 2, 3, 4]
my_list = ["string", 100, 23.2]

print(my_list)              # ['string', 100, 23.2]
print(my_list[0])           # string
print(len(my_list))         # 3


print(my_list[1:])          # [100, 23.2]
print(my_list[:1])          # string


# concatenate list 
mylist = ["one", "two", "three"]
extend_list = ["four", "five", "six"]
print(mylist + extend_list)         # ['one', 'two', 'three', 'four', 'five', 'six']

new_list = mylist + extend_list
new_list[0] = "changed string"
print(new_list)                     # ['changed string', 'two', 'three', 'four', 'five', 'six']

# append()
new_list.append("seven")
print(new_list)                     # ['changed string', 'two', 'three', 'four', 'five', 'six', 'seven']

# pop()
# pop(-1)       -1 is by default 
popped_item = new_list.pop()
print(new_list)                     # ['changed string', 'two', 'three', 'four', 'five', 'six']
print(popped_item)                  # seven

poped_item_sec = new_list.pop(-2)
print(poped_item_sec)               # five
print(new_list)                     # ['changed string', 'two', 'three', 'four', 'six']


# sort()
# hint: have to assign to a variable/ call the function first, otherwize will return None 
alph_list = ['a', 'e', 'x', 'b', 'c']
int_list = [4, 1, 5, 3, 8]
alph_list.sort()
print(alph_list)                    # ['a', 'b', 'c', 'e', 'x']

# 
# print(int_list.sort())                  # None

# int_list_assigned = int_list.sort()
# print(int_list_assigned)                # None
int_list.sort()
print(int_list)                         # [1, 3, 4, 5, 8]


# reverse()
int_list.reverse()
print(int_list)                     # [8, 5, 4, 3, 1]



