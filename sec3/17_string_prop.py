
# string is immutable(not changable)

name = "sam"
last_letters = name[1:]
print(last_letters)             # am 

# concatenate
print("p" + last_letters)       # pam


print("A" * 10)

symbol = "@"                    # AAAAAAAAAA
print(symbol * 10)              # @@@@@@@@@@


# attribute
x = "a whole string"
print(x.upper())                # A WHOLE STRING
print(x.lower())                # a whole string

# default split by white space
print(x.split())                # ['a', 'whole', 'string']
print(x.split("i"))             # ['a whole str', 'ng']









