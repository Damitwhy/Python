# Define a dictionary named 'payroll' that stores information about employees
payroll = {'emp1': {'name': 'Precious', 'job': 'Mgr', 'Wage': 50000},
           'emp2': {'name': 'Kim', 'job': 'Dev', 'Wage': 60000},
           'emp3': {'name': 'Sam', 'job': 'Dev', 'Wage': 70000}}

# Print the 'payroll' dictionary
print(payroll)

# Print the name of the employee with key 'emp1'
print(payroll['emp1']['name'])

# Print the value associated with the key 'salary' for the employee with key 'emp1'
print(payroll['emp1'].get('salary'))

# Print the value associated with the key 'Wage' for the employee with key 'emp1'
print(payroll['emp1'].get('Wage'))

# Add a new employee with key 'emp4' to the 'payroll' dictionary
payroll['emp4'] = {'name': 'Max', 'job': 'Admin', 'Wage': 30000}

# Print the updated 'payroll' dictionary
print(payroll)

# Remove the employee with key 'emp3' from the 'payroll' dictionary
del payroll['emp3']

# Iterate over the 'payroll' dictionary and print the employee ID and their information
for id, info in payroll.items():
    print(f'\nEmployee ID: {id}')
    for key in info:
        print(f'{key} : {info[key]}')

# Create the first dictionary for John Smith
john_dict = {
    "name": "John Smith",
    "email": "john@gmail.com",
    "subjects": ["Math", "Psychology", "Physics", "Chemistry", "Biology"]
}

# Create the second dictionary for Mary Jones
mary_dict = {
    "name": "Mary Jones",
    "email": "mary@gmail.com",
    "subjects": ["Fine Art", "Music", "Biology", "Geography", "Politics"]
}

# Create the student_data list containing both dictionaries
student_data = [john_dict, mary_dict]

# Print the student_data list
print(student_data)

# This is a one-line comment

"""
This is  multi-line comment.

We can spread this across as many lines as we need to
and it won't impact our computer program at all!!!
"""

import random

def lottery_generator():
    """
    Appends ten random numbers to an empty list
    Returns the list
    """
    numbers = [] # Empty list to hold the numbers
    for number in range(0, 10):
        # randint() generates random integers
        numbers.append(random.randint(1, 50))
    return numbers

print(f"This weeks winning lottery numbers are {lottery_generator()}")

import keyword

print(keyword.kwlist)

numbers = [4, 7, 12, 33, 13, 67]
remove = numbers.pop
print(remove())
print(remove(0))

integers = [1, 2, 3, 4, 5, 6]
def is_mult_of_three(n):
    return n % 3 == 0
    
print(list(filter(is_mult_of_three, integers)))

def my_decorator(func):
    def wrapper():
        print("The function has not been called yet. Let's call it.")
        func()
        print("The function was called and has returned a result.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")
    
say_hello()