from abc import ABC, abstractmethod

class humanBody(ABC):

    @abstractmethod
    def eyes(self):
        pass

class bodyParts(humanBody):
    pass

    def eyes(self):
        print("They provide capability to see")

    def ears(self):
        print("They provide capability to hear")

obj = bodyParts()
obj.eyes()
obj.ears()

print("********** Second Example **********")

from abc import ABC, abstractmethod

class Animal(ABC):

    # concrete method/normal method
    def sleep(self):
        print("Going to sleep in a while")

    # concrete method/normal method
    def eat(self):
        print("Start eating")

    @abstractmethod
    def sound(self):
        pass


class Snake(Animal):
    def sound(self):
        print("I hiss")


class Dog(Animal):
    def sound(self):
        print("I bark")


class Lion(Animal):
    def sound(self):
        print("I roar")

obj = Snake()
obj.sound()
obj = Dog()
obj.sound()
obj = Animal()
obj.sound()
