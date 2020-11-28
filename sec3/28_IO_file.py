
# # path
# MS 
# myfile = open("C:\\Users\\userNmae\\Folder\\text.txt")

# MacOS/ Linux
# myfile = open("/Users/UserName/Folder/text.txt") 



# under the same folder 

# %%writefile = my_new_file.txt

myFile = open('myfile.txt')

# if no such file exisiting 
# ileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'

print(myFile.read())
                        # This is an example 

                        # second line of txt 

                        # finishing editing 

# # reset cursor - reset cursor to the beginning position
# myFile.seek(0)

# .readline()
print(myFile.readline())

# have file closed 
myFile.close()


# This way dont need to worry to close()
# using new variable once opened the original
with open("myFile.txt") as my_new_file:
    contents = my_new_file.read()

print(contents)

                    # This is an example 

                    # second line of txt 

                    # finishing editing 



# # read
# with open("myFile.txt", mode = "r") as myfile:
# # read and writing 
# with open("myFile.txt", mode = "r+") as myfile:
    
# # write
# with open("myFile.txt", mode = "w") as myfile:
# # writing and reading (over write)
# with open("myFile.txt", mode = "w+") as myfile:
    
# # append
# with open("myFile.txt", mode = "a") as myfile:


with open("newCreate.txt", mode = "w") as f:
    f.write("I create this file with one line txt")

with open("newCreate.txt", mode = "r") as f:
    print(f.read())
