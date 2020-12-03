

# try: this block of code to be attempted ( may lead to error )
# except: block of code will execute in case there is an error in try block 
# finally: a fincal block of code to be executed, regardless of error 



# try:
#     # want to attemp 
#     # may have error 
# except:
#     print("hey it looks like you hit an error ")
# else:
#     # will run if no error 

# https://docs.python.org/3/library/exceptions.html

try: 
    # f = open("testfile", "w")
    f = open("testfile", "r")
    f.write("write a test line")
except TypeError:
    print("there was a type error")
except OSError:
    print("hey you have OS Error")
finally:
    print("I always run")


# hey you have OS Error
# I always run



def ask_for_int():
    try:
        result = int(input("Please provide a number"))
    except:
        print("Whoops sth went wrong")
    finally:
        print("End of try/ error/ finally")

print(ask_for_int())



def ask_for_int_while():
    while True:
        try:
            result = int(input("Please provide a number"))
        except:
            print("Whoops sth went wrong")
            continue
        else:
            print("all good")
            break
        finally:
            print("always running")

print(ask_for_int_while())







