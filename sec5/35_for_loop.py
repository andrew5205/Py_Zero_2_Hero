
# Pyhton object is Iterable = iterate over the object 

my_iterable_list = [1, 2, 3]

# placeholder 

for i in my_iterable_list:
    print(i)
                # 1
                # 2
                # 3


# common use _ for placeholder 
for _ in my_iterable_list:
    print("something")
                # something
                # something
                # something



myList = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

for num in myList:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number is {num}')


list_sum = 0
for num in myList:
    list_sum += num
print(list_sum)         # 55



# Tuple un-packing 
tup_list = [(1, 2), (3, 4), (5, 6)]
for ele in tup_list:
    print(ele)
    print(ele[0])
    print(ele[1])

for (a, b) in tup_list:
# for a, b in tup_list:
    print(a)
    print(b)



# dictionary - order NOT guarantee
myDict = {
    "k1": "val1",
    "k2": "val2",
    "k3": "val3",
}

for e in myDict.items():
    print(e)
    print(e[0])
    print(e[1])
    
for key, val in myDict.items():
    print(key)
    print(val)
    
for k in myDict.keys():
    print(k)
    
for v in myDict.values():
    print(v)

