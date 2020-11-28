
# .format()
# f-string 


# .format()
print('This is a string {}'.format("INSERTED"))             # This is a string INSERTED

print("The {} {} {}".format("fox", "brown", "quick"))       # The fox brown quick

print("The {0} {1} {2}".format("fox", "brown", "quick"))    # The fox brown quick
print("The {2} {1} {0}".format("fox", "brown", "quick"))    # The fox brown quick
print("The {0} {0} {0}".format("fox", "brown", "quick"))    # The fox fox fox

# assigned as variable inside format()
print("The {q} {b} {f}".format(f = "fox", b = "brown", q = "quick"))        # The quick brown fox



result = 100/777
print(result)                                       # 0.1287001287001287
print("The result was {}".format(result))           # The result was 0.1287001287001287
print("The result was {r}".format(r = result))      # The result was 0.1287001287001287

# {:width val}
print("The result was {r:.3f}".format(r = result))      # The result was 0.129
print("The result was {r:2.3f}".format(r = result))     # The result was 0.129
print("The result was {r:10.3f}".format(r = result))    # The result was      0.129

# truncating
str_truncating = "abcdefg"
print("{:.3}".format(str_truncating))               # abc
# {: # total width. #char}
str_truncating1 = "321.1234567"
print("{:.6}".format(str_truncating1))              # 321.12

print("{:4d}".format(42))                           # 00042
# sign
print("{:+d}".format(42))                           # +42


# name placeholder 
dictionary = {"first": "first_name", "last": "last_name"}
print("{first} {last}".format(**dictionary))                                # first_name last_name
print("{first} {last}".format(first = "firstName", last = "lastName"))      # firstName lastName

# getitem getattr
print("{d[first]} {d[last]}".format(d = dictionary))                        # first_name last_name
data_list = [0, 1, 2, 3, 4, 5, 6 ]
print({"{d[2]} {d[5]}".format(d = data_list)})                              # {'2 5'}

# accessing from attributes
class Plant(object):
    type = "tree from Plant class"
    kind = [{"name": "oak"}, {"name": "maple"}]
print("{p.type}".format(p = Plant))                                         # tree from Plant class
print("{p.type}: {p.kind[1][name]}".format(p = Plant))                      # tree from Plant class: maple


# Date time setup:
from datetime import datetime

print("{:%Y-%m-%d %H:%M}".format(datetime(2020, 11, 27, 12, 30)))           # 2020-11-27 12:30


dt = datetime(2020, 11, 27, 12, 50)
print("{:{dfmt} {tfmt}}".format(dt, dfmt = "%Y-%m-%d", tfmt = "%H:%M"))      # 2020-11-2712:50



# custom object
class HAL9000(object):
    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'
print('{:open-the-pod-bay-doors}'.format(HAL9000()))                         # I'm afraid I can't do that.



# f-string
name = "Jose"
age = 30
print(f"Hello, his name is {name}, he is {age} years old")      # Hello, his name is Jose, he is 30 years old



