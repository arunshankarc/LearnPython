def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total


my_list = [1, 2, 3, 4, 5]
print(sum_all_values(*my_list))
