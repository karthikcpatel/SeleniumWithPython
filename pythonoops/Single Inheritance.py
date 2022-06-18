class Teacher:

  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

class Student(Teacher):
  pass

obj = Student("Chetan", "Patel")
print(obj.firstname)
print(obj.lastname)