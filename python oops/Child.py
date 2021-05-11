#from python oops.Parent import Parent
from pythonoops.Parent import Parent

class ChildClass(Parent):
  pass

x = ChildClass("Kartik", "Patel")
x.printname()