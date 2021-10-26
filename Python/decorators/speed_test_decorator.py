from time import time
from functools import wraps


def speed_test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        print(f'Executing function {function.__name__}')
        result = function(*args, **kwargs)
        end_time = time()
        print(f'Elapsed time is {end_time - start_time}')
        return result
    return wrapper


@speed_test
def sum_nums_gen(max_nums):
    return sum(x for x in range(max_nums))


@speed_test
def sum_nums_list(max_nums):
    return sum([x for x in range(max_nums)])


max_nums = 90000000
print(sum_nums_gen(max_nums))
print(sum_nums_list(max_nums))
