
# # Syntax
# my_iterable = [1, 2, 3]
# for item in my_iterable:
#     print(item)



# for items not in my_iterable:
#     print(items)




my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in my_list:
    print(num)

                                    # 1
                                    # 2
                                    # 3
                                    # 4
                                    # 5
                                    # 6
                                    # 7
                                    # 8
                                    # 9

for e in my_list:
    if e % 2 == 0:
        print(e)
    else:
        print(f'odd number: {e}')
        
                                    # 0
                                    # odd number: 1
                                    # 2
                                    # odd number: 3
                                    # 4
                                    # odd number: 5
                                    # 6
                                    # odd number: 7
                                    # 8
                                    # odd number: 9

# define variable firt
list_sum = 0

for i in my_list:
    # list_sum = list_sum + i
    list_sum += i
    
print(list_sum)                     # 45


# loop through string 
my_string = "A part of all you earn is yours to keep"
for letter in my_string:
    print(letter)


# apply with tuple
tup = (1, 2, 3)
for t in tup:
    print(t)


my_tuple_list = [(1, 2), (3, 4), (5 ,6), (7, 8)]
print(len(my_tuple_list))           # 4

for ele in my_tuple_list:
    print(ele)
                                    # (1, 2)
                                    # (3, 4)
                                    # (5, 6)
                                    # (7, 8)

# use tuple packing => multiple variable pairs
# for (a, b) in my_tuple_list:
for a, b in my_tuple_list:
    print(a)
    print(b)

                                    # 1
                                    # 2
                                    # 3
                                    # 4
                                    # 5
                                    # 6
                                    # 7
                                    # 8


# apply with dictionary
# note: order is not guaranteed in dictionary
dict = {'key 1': 1, 'key 2': 2, 'key 3': 3}
for key, value in dict.items():
    print(key)
    print(value)

                                    # key 1
                                    # 1
                                    # key 2
                                    # 2
                                    # key 3
                                    # 3


# access only keys
for value in dict.keys():
    print(value)
                                    # key 1
                                    # key 2
                                    # key 3

# access only values 
for value in dict.values():
    print(value)
                                    # 1
                                    # 2
                                    # 3


