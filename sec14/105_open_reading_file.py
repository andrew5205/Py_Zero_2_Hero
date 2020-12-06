
# OS module & shutil module 



f = open("practice.txt", "w+")
f.write("this is the new string")
f.close()


import os 

# .getcwd()
print(os.getcwd())      # /Users/andrew/Desktop/udemy/Python zero to hero/sec14

# .listdir()
print(os.listdir())     # ['practice.txt', '103_Advance_module.py', '106_datetime.py', '105_open_reading_file.py', '104_collection.py']
# pass in any path
print(os.listdir("/Users/andrew/Desktop/udemy"))

# ***********************************************************************************************************

import shutil

# sh utility - linux like 
shutil.move("src", "dst")


# example to check folders & files 
# os.walk(File_path)
for folder, sub_folders, files in os.walk(os.getcwd()):
    print(f"\t Currently looking at {folder}")
    print("\n")
    print(f"The subfilder are:")
    for sub_fold in sub_folders:
        print(f"\t Subfolder: {sub_fold}")
        
    print("\n")
    print("The files are:")
    for f in files:
        print(f"\t Files are: {f}")
    print("\n")




