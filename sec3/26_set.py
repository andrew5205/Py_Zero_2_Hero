
# set are unordered collections of unique elements

# only one representative in one object


my_set = set()

my_set.add(1)
print(my_set)           # {1}


my_set.add(2)
my_set.add(3)
print(my_set)           # {1, 2, 3}


my_set.add(2)
print(my_set)           # {1, 2, 3}


un_org_list = [1,2,3,4,5,4,3,2,1]
# un_org_list.set()
print(set(un_org_list))         # {1, 2, 3, 4, 5}
