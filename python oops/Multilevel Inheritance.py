class Dhanji(ABC):

    def grandParent(self):
        print("Hey! I am the grandparent")

    def superMethodG(self):
        print("Someone has called super method from grandparent")

class Chetan(Dhanji):

    def parent(self):
        print("Hey! I am the parent")

    def superMethodP(self):
        print("Someone has called super method from parent")
        super().superMethodG()

class Kartik(Chetan):

    def child(self):
        print("Hey! I am the child")
        super().superMethodG()
        super().superMethodP()


x = Kartik()
x.grandParent()
x.parent()
x.child()