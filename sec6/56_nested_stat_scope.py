
# LEGB Rule:

# L: Local - name assigned within function
# E: Enclosing - name in local scope and all enclosing scope
# G: Global 
# B: Built-in


# Global
name = " This is a global name"

def greet():
    # enclosing
    name = "Sammy"
    
    def hello():
        # local
        name = " I'm from local"
        print("Hello " + name)    
    hello()

print(greet())          # Hello  I'm from local

# **************************************************************************

x = 50 

def funcX(x):
    print(f'X is {x}')
    
    # local statement 
    x =200 
    print(f'I just locally change X to {x}')


funcX(x)                # X is 50
                        # I just locally change X to 200



# **************************************************************************

y = 50 

def funcY():
    # use global key word, allowd to grab outta scope to glov=bal bariable 
    global y
    print(f'Y is {y}')
    
    # local statement, reaching to global variable, due to line 48
    y = "new value"
    print(f'I just locally change global Y to {y}')


funcY()                 # Y is 50
                        # I just locally change global Y to new value
