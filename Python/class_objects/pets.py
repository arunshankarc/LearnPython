"""
[Pet class]
You can access class attribute allowed_pets by self on each object too instead of class name Pet.
But the problem is that it can be updated like self.allowed = ["rat"] from say, dog object.
Now this will cut the reference of dog object's allowed_pets to Pet and
create its own allowed list thus defeating the purpose of class attribute.
"""

class Pet:
    """
    [Pet class which checks if a given pet can be a pet or not.]
    """
    # allowed is a class attribute
    allowed_pets = ["rat", "dog", "cat", "fish"]
    def __init__(self, name, species):
        if species not in Pet.allowed_pets:
            raise ValueError(f"You cannot have {species} as pet")
        self.name = name
        self.species = species

    def set_species(self, species):
        """[Set species]

        Args:
            species ([str]): [species]

        Raises:
            ValueError: [If species not in allowed]
        """
        if species not in Pet.allowed_pets:
            raise ValueError(f"You cannot have {species} as pet")
        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
dog.species = "tiger"
print(dog.species)
print(id(cat.allowed_pets))
print(id(dog.allowed_pets))
print(id(Pet.allowed_pets))
