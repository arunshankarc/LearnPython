"""
+ operator is shorthand for __add__() that gets called on first operand.
First operand is important because in __add__ or __mul__ first gets passed automatically
while second we need to check for type (see methods __add__ or __mul__).

Checks type on first operand and calls respective class:
8 + 3  # int
"8" + "3" # String

len uses __len__()
"""

from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        # When you add two humans together...you get a newborn baby Human!
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        # When you multiply a Human by an int, you get clones of that Human!
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "CANT MULTIPLY!"

j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
# print(j)
# print(len(j))
# triplets = j * 3

# kevin and jessica have triplets!
triplets = (k + j) * 3
print(triplets)
