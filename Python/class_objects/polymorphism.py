"""
[Example for polymorphism in classes]
Same method name in multiple places but depends on who calls it.
Single method taken multiple forms.

Common example also in Python is:

8 + 2
"A" + "B"

or:

len([1, 2, 3])
len("Arun")
"""

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof!!"


class Cat(Animal):
    def speak(self):
        return "Meow!!"


class Fish(Animal):
    pass


d = Dog()
print(d.speak())
f = Fish()
print(f.speak())
