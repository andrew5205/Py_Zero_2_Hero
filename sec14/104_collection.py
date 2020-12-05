
# Collections Module

from collections import Counter
# counter is basically a dictionary sub-class

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3]
print(Counter(mylist))          # Counter({3: 8, 1: 5, 2: 4})   --> object


string_list = ["a", "a", 2, 2, 2, 2]
print(Counter(string_list))     # Counter({2: 4, 'a': 2})   -- object


print(Counter("aaaabbbbbbcccedrrrr"))       # Counter({'b': 6, 'a': 4, 'r': 4, 'c': 3, 'e': 1, 'd': 1})



# split()
sayin = "a aprt of all you earn is yours to keep"
print(sayin.split())                    # ['a', 'aprt', 'of', 'all', 'you', 'earn', 'is', 'yours', 'to', 'keep']

print(Counter(sayin))                   # Counter({' ': 9, 'a': 4, 'o': 4, 'r': 3, 'e': 3, 'p': 2, 't': 2, 'l': 2, 'y': 2, 'u': 2, 's': 2, 'f': 1, 'n': 1, 'i': 1, 'k': 1})
print(Counter(sayin.split()))           # Counter({'a': 1, 'aprt': 1, 'of': 1, 'all': 1, 'you': 1, 'earn': 1, 'is': 1, 'yours': 1, 'to': 1, 'keep': 1})
print(Counter(sayin.upper().split()))   # Counter({'A': 1, 'APRT': 1, 'OF': 1, 'ALL': 1, 'YOU': 1, 'EARN': 1, 'IS': 1, 'YOURS': 1, 'TO': 1, 'KEEP': 1})


letters = "aaaaaaabbbbbbbbccccccccccccccccdddddeeeeeeeeeeeeeee"
c = Counter(letters)
print(c.most_common())                      # <bound method Counter.most_common of Counter({'c': 16, 'e': 15, 'b': 8, 'a': 7, 'd': 5})>
print(c.most_common(2))                     # [('c', 16), ('e', 15)]
# print(c.most_common()[:-n-1:-1])            # n least common items 
print(c.most_common()[:-5-1:-1])            # [('d', 5), ('a', 7), ('b', 8), ('e', 15), ('c', 16)]

print(sum(c.values()))                      # 51
# print(c.clear())                            # None
print(list(c))                              # ['a', 'b', 'c', 'd', 'e']
print(dict(c))                              # {'a': 7, 'b': 8, 'c': 16, 'd': 5, 'e': 15}
print(c.items())                            # dict_items([('a', 7), ('b', 8), ('c', 16), ('d', 5), ('e', 15)])
print(c.keys())                             # dict_keys(['a', 'b', 'c', 'd', 'e'])
print(c.values())                           # dict_values([7, 8, 16, 5, 15])
# ************************************************************************************************************************************


# default dictionary - prevent unassign error from dict 
from collections import defaultdict

# use lambda to assign default val
d = defaultdict(lambda: 50)

d["assigned"] = 100
print(d["assigned"])            # 100

print(d["not yet"])             # 50

print(d)                        # defaultdict(<function <lambda> at 0x7fd02b098d30>, {'assigned': 100, 'not yet': 50})
# ************************************************************************************************************************************


from collections import namedtuple

# OOP concept
#                 Type      attribute 
DogT = namedtuple("Dog", ["age", "breed", "name"])

sammy = DogT(age = 5, breed = "Husky", name = "Sam")

print(sammy)            # Dog(age=5, breed='Husky', name='Sam')
print(sammy.age)        # 5
print(sammy[0])         # 5

print(sammy.breed)      # Husky
print(sammy[1])         # Husky

print(sammy.name)       # Sam
print(sammy[2])         # Sam

