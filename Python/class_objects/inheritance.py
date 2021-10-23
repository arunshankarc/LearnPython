"""
[Animal class]
Each animal has a name and species.
Cat is an animal which also has a breed and its fav toy.
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is an {self.species}."

    def make_sound(self, sound):
        print(f"{self.name} animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def __repr__(self):
        return f"{self.name} is a {self.species} and calling from Cat class."

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")
print(blue)
