

# Comprehension

# dictionary comprehension
dict_comp = {x: x ** 2 for x in range(10)}
print(dict_comp)            # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

dict_comp2 = {v.upper(): v * 3 for v in "coding"}
print(dict_comp2)           # {'C': 'ccc', 'O': 'ooo', 'D': 'ddd', 'I': 'iii', 'N': 'nnn', 'G': 'ggg'}

# using zip 
dict_comp3 = {k: v * 2 for k, v in zip(range(3), range(10, 60, 10))}
print(dict_comp3)           # {0: 20, 1: 40, 2: 60}

dict_comp4 = {k: v ** 2 for k, v in zip(["a", "b"], range(2))}
print(dict_comp4)           # {'a': 0, 'b': 1}



# list comprehension
list_comp = [x ** 2 for x in range(10)]
print(list_comp)            # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




d = {'k1': 1, 'k2': 2}
# items()
# keys()
# values()
for k in d.items():
    print(k)



















