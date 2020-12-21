
# s.add()
# s.clear()
# s.copy() - shollow copy 

# s.difference() - set1.difference(set2)
# s.intersection() - set1.intersection(set2)
# s.symmetric_difference()

# s.difference_update() - set1.difference_update(set2) - update set1 with differences
# s.intersection_update() - set1.intersection_update(set2) - update set1 with intersection
# s.symmetric_difference_update()

# s.discard() - remove element from set

# s.isdisjoint()
# s.issubset()
# s.issuperset()

# s.union() - s1.union(s2)
# s.update() - s1update(s2)





s = set()

s.add(1)
s.add(2)


print(s)        # {1, 2}


s.clear()
print(s)        # set()


s = {1, 2, 3}

sc = s.copy()
print(sc)       # {1, 2, 3}

s.add(4)
print(s.difference(sc))     # {4}


# s.intersection() - set1.intersection(set2) 
s1 = {1,2,3}
s2 = {1,2,4}

print(s1.intersection(s2))      # {1, 2}
#################################################################################


# s.difference_update() - set1.difference_update(set2) - update set1 with differences
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(s1)           # {2, 3}


# s.intersection_update() - set1.intersection_update(set2) - update set1 with intersection
s1 = {1,2,3}
s2 = {1,2,4}
s1.intersection_update(s2)
print(s1)                       # {1, 2}


# s.symmetric_difference() set1.symmetric_difference(set2) - 
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.symmetric_difference(s2))      # {3, 4}

s1.symmetric_difference_update(s2)
print(s1)


ss = {1,2,3,4,5}
ss.discard(3)
print(ss)           # {1, 2, 4, 5}




ss1 = {1, 2, 3}
ss2 = {1, 2, 4}
ss3 = {5, 6}
print(ss1.isdisjoint(ss2))      # False 
print(ss1.isdisjoint(ss3))      # True




sub1 = {1, 2}
sub2 = {1, 2, 3, 4, 5}
print(sub1.issubset(sub2))      # True
print(sub2.issuperset(sub1))    # True



su1 = {1,2,4}
su2 = {1,3,5,7}
print(su1.union(su2))           # {1, 2, 3, 4, 5, 7}

su1.update(su2)
print(su1)                      # {1, 2, 3, 4, 5, 7}

