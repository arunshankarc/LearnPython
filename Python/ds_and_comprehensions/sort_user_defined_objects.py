class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = int(age)

    def __repr__(self):
        return f"{self.name} is of {self.age} years and draws salary of {self.salary}"


def e_sort(emp):
    return emp.age


e1 = Employee('Arun', '33', '10000')
e2 = Employee('Kavya', '30', '1000')
e3 = Employee('Nithya', '5', '500')
emp_list = [e1, e2, e3]

sorted_list = sorted(emp_list, key=e_sort)
print(sorted_list)
