class Dog:
    species = "Canis lupus"  # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_species(cls, species_name):
        cls.species = species_name

    def bark(self):
        return f"{self.name} says woof!"

# Accessing the class method
Dog.set_species("Canis familiaris")

# Create an instance of Dog
my_dog = Dog("Buddy", 3)
print(my_dog.species)  # Output: Canis familiaris