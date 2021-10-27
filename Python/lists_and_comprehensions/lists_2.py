courses = ['History', 'Maths', 'Physics', 'Compsci']
courses_2 = ['Arts', 'DS']

courses.extend(courses_2)
print(courses)
courses.append('Test')
print(courses)
courses.insert(1, 'Check')
print(courses)
courses.remove('Check') # element based
print(courses)
courses.pop(2) # index based 
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)

# sorted does not sort in place like .sort()

nums = [2, 1, 4, 3]
print(sorted(nums))
print(min(nums))
print(max(nums))
print(sum(nums))

# Get index of specific element

print(courses.index('Maths'))

# check if element is present

print('Math' in courses)
print('Maths' in courses)

# Get index of each value in list

for index, course in enumerate(courses):
    print(f"{index} {course}")

# If you don't want to start from 0 as index

for index, course in enumerate(courses, start=1):
    print(f"{index} {course}")

course_str = ",".join(courses)
print(course_str)

splitted_string = course_str.split(',')
print(splitted_string)


## tuples and sets  ##
# Sets, Lists - mutable
# Tuples - immutable - all actions on list other than removal/modification does not apply
# Sets are best for situations where duplicates not allowed, intersection, difference, union kind
# of operation. Also, sets does not keep the index as it is for records.
# Sets are efficient in scenarios where 'Test' in my_set kind of operations in loops.

my_set = {'History', 'Maths', 'Physics', 'Compsci', 'Compsci'}
print(my_set.pop())
print(my_set.pop())
print(my_set)
my_set.add('Physics') # similar to append
print(my_set)
my_set2 = {'Arts', 'Design'}
my_set.update(my_set2) # similar to extend or union
print(my_set)
my_set.remove('Design')
print(my_set)
my_set3 = {'Economics', 'Geography', 'Design', 'Compsci', 'Physics'}
print(f"my_set : {my_set}")
print(f"my_set3 : {my_set3}")
print(my_set.intersection(my_set3))
print(my_set.union(my_set3))
print(my_set.difference(my_set3))
