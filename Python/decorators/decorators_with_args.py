def ensure_first_arg(value):
    def inner(function):
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                raise ValueError(f"First arg needs to be {value}")
            else:
                return function(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg(10)
def add_to_ten(num_1, num_2):
    return num_1 + num_2


print(add_to_ten(10, 20))
print(add_to_ten(1, 20))
