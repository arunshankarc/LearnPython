"""
[User class]
_name ==> Convention wise private - nothing stops not to use this
__name__ ==> Similar to __init__() or dunder methods (python specific methods)
__name ==> This is called name mangling where the variable is changed to _<class_name>__<variable>
So __name becomes _Person__name
Name mangling is used when same variable needs to be used by child classes in inheritance
and they can use same names under different classes


__repr__ => Represents/Representation similar to to_string() in java
"""

class User:
    """
    [This is a user class for learning]
    first, last and age are instance/object attributes
    """

    # class attribute
    active_users = 0

    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age
        self._emp_salary = 10000
        self.__msg = "This person was added when company's BU - test was under immense loss"
        User.active_users += 1

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is of age {self.age} " \
               f"years and draws a salary/pension of {self._emp_salary}."

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
        """
        [What does the user like?]

        Args:
            what_likes ([str]): [likings]

        Returns:
            [str]: [Returns the user likes]
        """
        return f"{self.first_name} {self.last_name} likes {what_likes}"

    def is_senior(self):
        """
        [Is senior]

        Returns:
            [boolean]: [True or False]
        """
        return self.age >= 65

    def logout(self):
        """
        [Logout of application]
        """
        User.active_users -= 1
        return f"{self.first_name} {self.last_name} logged out so number of active users is " \
            f"{User.active_users}"

    @classmethod
    def say_hi(cls):
        """
        [Static method to say hi]
        """
        print("Hello")

    @classmethod
    def display_active_users(cls):
        """
        [Display active users]

        Returns:
            [str]: [number of active users string]
        """
        return f"There are currently {cls.active_users} users."

    @classmethod
    def read_create_object(cls, data_string):
        """
        [What if we have csv input, handle it by reading input]

        Args:
            data_string ([str]): [csv string]

        Returns:
            [object]: [User object]
        """
        first, last, age = data_string.split(',')
        return cls(first, last, int(age))


print(f"{User.active_users} active users")
user1 = User("Arun", "Shankar", 33)
user2 = User("Nithya", "Shree", 5)
print(f"{User.active_users} active users")
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
print(user1.logout())
user1 = User("Arun", "Shankar", 33)
# Invoke class methods using class name instead of object name to avoid confusion.
# Python never restricts though.
print(User.display_active_users())
print(user2.display_active_users())

# Use class method read_create_object and create an object using csv input
user_joe = User.read_create_object("Joe,Smith,66")
print(user_joe.full_name())
print(user_joe.initials())
print(user_joe.is_senior())


# Test out __repr__ usage.
print(user_joe)
