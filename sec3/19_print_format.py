
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








# f-string
name = "Jose"
age = 30
print(f"Hello, his name is {name}, he is {age} years old")      # Hello, his name is Jose, he is 30 years old



