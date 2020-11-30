
def execute_func():
    print("executed")


execute_func()                  # executed
print(type(execute_func))       # <class 'function'>


# def func_name(parameter)
# set parameter = "Default" to prevent error 

# call a function, will take arguements

def say_name(name = "Default"):
    print(f'My name is {name}')

say_name("Andrew")              # My name is Andrew
say_name("")                    # My name is 









