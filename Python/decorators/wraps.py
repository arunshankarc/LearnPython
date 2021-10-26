"""
[wraps brings in the actual doc string of the actual function instead of wrapper.
Just comment and uncomment wraps(function) to understand more.
The difference is without @wraps it gives doc string of wrapper while
with @wraps we get doc string of add function.]
"""

from functools import wraps


def provide_function_details(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        """[Wrapper function]

        Returns:
            [function]: [called function]
        """
        print(f'The function name that is called is {function.__name__}')
        print(f'The function doc string is {function.__doc__}')
        return function(*args, **kwargs)
    return wrapper


@provide_function_details
def add(number_1, number_2):
    """Adds 2 numbers

    Args:
        a ([int]): [int]
        b ([int]): [int]

    Returns:
        [int]: [added numbers]
    """
    return number_1+number_2


print(add(5, 6))
help(add)
