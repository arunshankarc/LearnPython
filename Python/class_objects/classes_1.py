"""
 _name ==> Convention wise private - nothing stops not to use this
 __name__ ==> Similar to __init__() or dunder methods (python specific methods)
 __name ==> This is called name mangling where the variable is changed to _<class_name>__<variable>
 So __name becomes _Person__name
 Name mangling is used when same variable needs to be used by child classes in inheritance
 and they can use same names under different classes
"""

class User:
    """
    [This is a user class for learning]
    first, last and age are instance/object attributes
    """
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age
        self._emp_salary = 10000
        self.__msg = "This person was added when company's BU - test was under immense loss"

    def full_name(self):
        """
        Return Full name

        Returns:
            str: full name
        """
        return f"{self.first_name} {self.last_name}"

    def initials(self):
        """
        [Return initials]

        Returns:
            [str]: [intials]
        """
        return f"{self.first_name[0]}. {self.last_name[0]}."

    def likes(self, what_likes):
        """[What does the user like?]

        Args:
            what_likes ([str]): [likings]

        Returns:
            [str]: [Returns the user likes]
        """
        return f"{self.first_name} {self.last_name} likes {what_likes}"

    def is_senior(self):
        """[Is senior]

        Returns:
            [boolean]: [True or False]
        """
        return self.age >= 65

    def say_hi():
        """
        [Static method to say hi]
        """
        print("Hello")


user1 = User("Arun", "Shankar", 33)
user2 = User("Nithya", "Shree", 5)
print(user1)
print(type(user1))
# Below line fails because of name mangling
# print("==> " + user1.__msg)
print(dir(user1)) # prints all the scope variables
print(user1.full_name())
print(user2.full_name())
print(user1.initials())
print(user2.initials())
print(user1.is_senior())
print(user2.is_senior())

# user1.say_hi() # Throws error
User.say_hi() # This is nothing but like static method
