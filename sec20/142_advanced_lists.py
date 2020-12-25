
# list.append()
# list.count()
# list.copy()

# list.extend()

# list.index()
# list.insert() - insert(index, value)
# list.pop()
# list.remove() - remove(value)
# list.reverse()


l = [1, 2, 3]
l.append(4)
print(l)            # [1, 2, 3, 4]

print(l.count(2))   # 1
print(l.count(100)) # 0



list_x = [ 1, 2, 3]
list_x.extend([4,5,6])
print(list_x)       # [1, 2, 3, 4, 5, 6]


list_y = [2, 4, 6]
print(list_y.index(6))          # 2

list_y.insert(2, "inserted")
print(list_y)                   # [2, 4, 'inserted', 6]


print(list_y.pop())             # 6
print(list_y)                   # [2, 4, 'inserted']

print(list_y.pop(0))            # 2
print(list_y)                   # 4, 'inserted']


list_z = [1, 3, 5, 7 ,9 ,11]
list_z.remove(5)
print(list_z)                   # [1, 3, 7, 9, 11]


random = [ 5, 2, 6, 3, 8, 1 ,9 ,7]
random.sort()
print(random)

random.reverse()
print(random)                   # [9, 8, 7, 6, 5, 3, 2, 1]


coppy = random.sort()
print(coppy)                    # None

random.sort()
right_cop = random.copy()
print(right_cop)                # [1, 2, 3, 5, 6, 7, 8, 9]