
# myList = [1, 2, 3]

# in range(start, end, step)
for num in range(10):
    print(num)
    
# start 3 to 10(not included)
for num in range(3,10):
    print(num)


# Generator
fast_list = list(range(0,11,2))
print(fast_list)                    # [0, 2, 4, 6, 8, 10]


# *********************************************************************
# enumerate
index_count = 0
word = "abcde"
for letter in word:
    print("At index {} the letter is {}".format(index_count, letter))

# enumerate
for item in enumerate(word):
    print(item)
                        # (0, 'a')
                        # (1, 'b')
                        # (2, 'c')
                        # (3, 'd')
                        # (4, 'e')


for i, element in enumerate(word):
    print(i)
    print(element)



# *********************************************************************
# zip()
# match the shortest len, ignore extra element 
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = ["extra", "extra", "extra"]

my_zipped = zip(list1, list2,list3)
print(my_zipped)                # <zip object at 0x7fa4a530cc00> show you only the place store in memory


for item in my_zipped:
    print(item)
                                # (1, 'a', 'extra')
                                # (2, 'b', 'extra')
                                # (3, 'c', 'extra')


print(list(zip(list1, list2)))      # [(1, 'a'), (2, 'b'), (3, 'c')]



# *********************************************************************
# in

alpList = ["a", "b", "c", "d", "e", "f", "g"]
print("a" in alpList)           # True
print("z" not in alpList)       # True



# *********************************************************************
# min()
# max()
num_list = [1, 2, 3, 50, 100]
print(min(num_list))            # 1
print(max(num_list))            # 100


# random library
from random import shuffle
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(my_list)
print(my_list)                  # [3, 6, 1, 5, 8, 4, 2, 7, 9, 10]


from random import randint
print(randint(0, 1000))


# *********************************************************************
# input - always takes in as a STRING
input(" please input a num here: ")

# conver input to int 
result = int(input(" please input a num here: "))

