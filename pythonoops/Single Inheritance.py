class Teacher:

  print("Default constructor is invoked")
  # def __init__(self, fname, lname):
  #   self.firstname = fname
  #   self.lastname = lname



class Student(Teacher):
  pass

obj = Student()
# As soon as an ibject of class is created a constructor would be invoked.
# If we explicitly create a constructor with some request, it would serve that request
