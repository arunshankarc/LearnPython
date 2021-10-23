"""
[MRO - Method Resolution Order]
Understand the order of resolution of methods
"""

class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"


class Child(Mother, Father):
    pass


print(Child.__mro__)
print(Child.mro())
help(Child)