"""
[Learning multiple inheritance]
Please see the comments in __init__() method of Penguin which explains the confusion.
"""

class Aquatic:
    """
    [Aquatic animals]
    """
    def __init__(self, name):
        print("Aquatic Init!!")
        self.name = name

    def swim(self):
        """[Swim]

        Returns:
            [str]: [description]
        """
        return f"{self.name} is swimming."

    def greet(self):
        """[Greet]

        Returns:
            [str]: [description]
        """
        return f"I am {self.name} of the sea."


class Ambulatory:
    """
    [Land animals]
    """
    def __init__(self, name):
        print("Ambulatory Init!!")
        self.name = name

    def walk(self):
        """[Walking]

        Returns:
            [str]: [description]
        """
        return f"{self.name} is walking."

    def greet(self):
        """[Greet]

        Returns:
            [str]: [description]
        """
        return f"I am {self.name} of the land."


class Penguin(Aquatic, Ambulatory):
    """
    [Penguin]
    """
    def __init__(self, name):
        print("Penguin Init!!")
        # Only first class inherited super() is called and not second one.
        # In this case only Aquatic __init__() is called and not Ambulatory.
        # super().__init__(name)
        # But lets say we need both __init__ to be called then
        # it needs to be mentioned explicitly.
        # But now you can see that things got complicated and now there is only 
        # one variable name which caused confusion.
        # So, that is the disadvantage of multiple inheritance.
        Aquatic.__init__(self, name)
        Ambulatory.__init__(self, name)


# jaws = Aquatic("Jaws")
# lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")
print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet()) # Taking from first class inherited i.e. Aquatic
# check which instance it is?
print(f"captain_cook is instance of {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of {isinstance(captain_cook, Ambulatory)}")
print(f"captain_cook is instance of {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of {isinstance(captain_cook, object)}")
