student = {'name': 'arun', 'age': 33, 'courses': ['CompScie', 'AWS']}

for key in student:
    print(key)


for value in student.values():
    print(value)


for k, v in student.items():
    print(k, v)

age = student.pop('age')
print(student)
print(age)

del student['name']
print(student)

student = {'name': 'arun', 'age': 33, 'courses': ['CompScie', 'AWS']}
