class Person:
    species = "Human"  # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_baby(cls, name):
        # A factory method that creates an instance with a default age
        return cls(name, age=0)

    @classmethod
    def set_species(cls, species_name):
        # Modifies the class attribute
        cls.species = species_name


# Creating instances using the factory method
baby = Person.create_baby("John")
print(baby.name)  # Output: John
print(baby.age)   # Output: 0

# Accessing and modifying the class attribute
print(Person.species)  # Output: Human
Person.set_species("Alien")
print(Person.species)  # Output: Alien
