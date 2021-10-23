"""
[User]
This example shows how to use getters and setters in python
"""

class User:
    """
    [User class where we set parameters for user]
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        if User._check_age(age):
            self._age = age
        else:
            raise ValueError(f"Age {age} is not greater than 0 or less than 120.")

    # Below is getter
    @property
    def age(self):
        """[set age]

        Returns:
            [int]: [return age]
        """
        return self._age

    # Below is setter
    @age.setter
    def age(self, new_age):
        if User._check_age(new_age):
            self._age = new_age
        else:
            raise ValueError(f"Age {new_age} is not greater than 0 or less than 120.")

    @property
    def full_name(self):
        """[return full_name]

        Returns:
            [str]: [full name]
        """
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, new_full_name):
        self.first_name, self.last_name = new_full_name.split(' ')

    @classmethod
    def _check_age(cls, age):
        return age > 0 or age <= 120


arun = User("Arun", "Shankar", 33)
print(arun.age)
arun.age = 50
print(arun.age)
