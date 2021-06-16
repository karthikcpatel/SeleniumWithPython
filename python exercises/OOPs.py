#1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        print(self.max_speed,self.mileage)

obj = Vehicle(100,15)

#2. Create a Vehicle class without any variables and methods
class Vehicle:
    pass

#3. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_All(self):
        print(self.name,self.max_speed,self.mileage)

class Bus(Vehicle):
    pass

obj = Bus("School Volvo", 180, 12)
obj.print_All()

#4. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class. You need to use method overriding.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
