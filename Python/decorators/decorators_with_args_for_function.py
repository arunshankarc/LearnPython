"""
[Just add args and kwargs]
"""


def shout(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}"


@shout
def order(main, side):
    return f"Hi, I'd like to have {main} with the {side} on the side please."


print(greet('Arun'))
print(order('Masala Dose', 'Coffee'))
