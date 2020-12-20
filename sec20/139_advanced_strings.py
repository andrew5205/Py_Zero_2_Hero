
# built-in
# str.capitalize()
# str.title()
# str.upper()
# str.upper()
# str.count() - return int
# str.find() - return index 
# str.center(a, b)
# str.expandtabs()

# str.isalnum()
# str.isalpha()
# str.isascii()
# str.islower()
# str.isspace()
# str.istitle()

# str.rstrip() - trim right space 
# str.strip() - trim all space 
# str.lstrip() - trim left space

# str.startswith()
# str.endswith()

# str.split()
# str.partition() - return tuple string


s = "hello world"
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.count("o"))
print(s.find("o"))


# total 20 space, in center of z's
print(s.center(20, "z"))        # zzzzhello worldzzzzz


# \t => tab
print('hello\tworld')           # hello   world

print('hello\tworld'.expandtabs())      # hello   world


print(s.isalnum())      # False   # number or alph-anumeric, but not space
print(s.isalpha())      # Fasle   # alph-anumeric, but not space
print(s.isascii())      # True    # space is also ASCII

print(s.islower())      # True 
print(s.isspace())      # False

t = "   three space in front, three space in the back   "
print(t.rstrip())       #    three space in front, three space in the back
print(t.strip())        # three space in front, three space in the back
print(t.lstrip())       # three space in front, three space in the back   


print(s.startswith("h"))        # True
print(s[0] == "h")              # True
print(s.endswith('d'))          # True
print(s[-1] == "o")             # False




# REGULAR EXPRESSION

u = "a part of all you earn, is your to keep"

# split() - will drop seperator
print(u.split())        # ['a', 'part', 'of', 'all', 'you', 'earn,', 'is', 'your', 'to', 'keep']
print(u.split(" "))     # ['a', 'part', 'of', 'all', 'you', 'earn,', 'is', 'your', 'to', 'keep']
print(u.split(","))     # ['a part of all you earn', ' is your to keep']
print(u.split("o"))     # ['a part ', 'f all y', 'u earn, is y', 'ur t', ' keep']

# .partition() return a tuple, including seperator
print(u.partition(",")) # ('a part of all you earn', ',', ' is your to keep')




