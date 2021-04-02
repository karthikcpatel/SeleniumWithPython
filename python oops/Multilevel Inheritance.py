class Dhanji:

    def grandParent(self):
        print("Hey! I am the grandparent")

class Chetan(Dhanji):

    def parent(self):
        print("Hey! I am the parent")


class Kartik(Chetan):

    def child(self):
        print("Hey! I am the child")

x = Kartik()
x.grandParent()
x.parent()
x.child()