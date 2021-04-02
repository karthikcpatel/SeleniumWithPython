# Global variable is defined outside the class. It can be accessed globally.
# Local variable inside the method. It can be accessed through an object.
# If local variable is not present inside method it will search for global variable.

gvar = "Chetan"

def globallocal():

    global gvar
    gvar = "Kartik"
    lvar = "Dipika"

    print(gvar,lvar)

    print("Hello. This is a normal function")

globallocal()
print(gvar)