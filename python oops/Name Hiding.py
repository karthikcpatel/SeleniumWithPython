# In below example __lastname is private
class Person:
    def __init__(self):
        self.name = 'Kartik'
        self.__lastname = 'Patel'

    def PrintName(self):
        return self.name + ' ' + self.__lastname


# Outside class
P = Person()
print(P.name)
print(P.PrintName())
print(P._Person__lastname)
