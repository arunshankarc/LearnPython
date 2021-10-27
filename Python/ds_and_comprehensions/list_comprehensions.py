nums = [1 ,2, 3, 4, 5]
my_list = []
for num in nums:
    my_list.append(num)

my_list = []
my_list = [num for num in nums]


# Find even numbers
my_list = []
for num in range(10):
    if num % 2 == 0:
        my_list.append(num)

print(my_list)

my_list = [num for num in range(10) if num % 2 == 0]
print(my_list)
my_list = []
# concat an alphabet and a number
for alphabet in 'abcde':
    for num in range(5):
        my_list.append((alphabet, num))

print(my_list)

my_list = [(alphabet, num) for alphabet in 'abcde' for num in range(5)]
print(my_list)

# Dictionary comprehension

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero

print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

# If i don't want to add Peter
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict)

# If I don't want spiderman
my_dict = {name: hero for name, hero in zip(names, heroes) if hero != 'Spiderman'}
print(my_dict)
