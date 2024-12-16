# Global variable is defined outside the class. It can be accessed globally.
# Local variable inside the method. It can be accessed through an object.
# If local variable is not present inside method it will search for global variable.
# https://www.geeksforgeeks.org/global-local-variables-python/

gvar = "Chetan"

def globallocal():

    global gvar
    gvar = "Kartik"
    lvar = "Bindu"

    print(gvar,lvar)

    print("Hello. This is a normal function")

print(gvar)
globallocal()
print(gvar)