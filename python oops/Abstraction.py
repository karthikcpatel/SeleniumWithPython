from abc import ABC, abstractmethod

class humanBody(ABC):

    @abstractmethod
    def eyes(self):
        print("They provide capability to seeyuyi")

class bodyParts(humanBody):
    pass

    def eyes(self):
        print("They provide capability to see")

    def ears(self):
        print("They provide capability to hear")

obj = bodyParts()
obj.eyes()
obj.ears()