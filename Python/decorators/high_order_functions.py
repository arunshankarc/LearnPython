"""
[In simple terms, if a function has another function as arguments or returns another function
, then that function is called an higher order function. If a function is inside
another function (nested), then its higher order as well.]
"""
from random import choice


def square_cube(number, func):
    """[Return Square or cube i.e. pasing function as arguments]

    Args:
        number ([int]): [number to sq or cube]
        func ([function]): [what to run?]

    Returns:
        [int]: [Square or cube]
    """
    total = 0
    for num in range(1, number+1):
        total += func(num)
    return total


def _square(num):
    return num*num


def _cube(num):
    return num*num*num


def greet(name):
    """[Function inside another function.]

    Args:
        name ([str]): [name]

    Returns:
        [str]: [mood]
    """
    def get_mood():
        return choice(['Hello there, ', 'Go away, ', 'I love you'])
    return get_mood() + f" {name}"


def make_laugh_func():
    """
    [Return function to the caller.]
    """
    def get_laugh():
        return choice(('lol', 'Hehehehehehe', 'HAHAHAHHAHA'))
    return get_laugh


def make_laugh_func_args(name):
    """
    [Return function to the caller but now with args.
    The args are also accessed by inner functions.
    Also, called closures in python.
    Similar to decorators.]
    """
    def get_laugh():
        return choice(('lol', 'Hehehehehehe', 'HAHAHAHHAHA')) + f' {name}'
    return get_laugh


print(square_cube(5, _square))
print(square_cube(5, _cube))
print(greet('Arun'))
laugh = make_laugh_func()
print(laugh())
laugh_person = make_laugh_func_args("Arun")
print(laugh_person())
print(laugh_person())
print(laugh_person())
print(laugh_person())
