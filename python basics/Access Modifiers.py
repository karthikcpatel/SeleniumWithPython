# We have three different type of access modifiers: public, private, protected
# public - accessible to everyone
# protected - accessible to only in the class and outside the class through inheritance
# private - accessible only in the class. We need to append name to class in order to access private variables and methods

class AccessModifiers:
    public = "This is a public variable"
    _protect = "This is a protected variable"
    __private = "This is a private variable"
    def _init_(self):
        print("The constructor is initialized")

x = AccessModifiers()
print(x.public)
print(x._protect)
print(x._AccessModifiers__private)