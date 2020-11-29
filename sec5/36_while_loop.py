
# run while sth is True


# while condition:
#     do something
# else:
#     do the rest



x = 0

while x < 5:
    print({f'current a is {x}'})
    x += 1
else:
    print("out of range 5 ")

                                    # {'current a is 0'}
                                    # {'current a is 1'}
                                    # {'current a is 2'}
                                    # {'current a is 3'}
                                    # {'current a is 4'}
                                    # out of range 5 





# break - break out of the loop 
# continue - continuew doing anyway 
# pass - not do anything at all, and running the next

x = [1, 2, 3]

for item in x:
    pass 
print("this is the end")        # this is the end


myString = "part of all you earn is yours to keep"

for char in myString:
    if char == "e":             # continue will pass this condition
        continue
    print(char)


for alp in myString:
    if char == "o":             # break will exit the loop when this condition meet
        break
    print(alp)



