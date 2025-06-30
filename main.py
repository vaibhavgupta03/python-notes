# File: /python-notes/python-notes/main.py

# This is the main script for the Python notes project. 
# It contains examples and exercises related to the concepts covered in the chapters.

# Example of printing a message
print("Welcome to the Python Notes Project!")

# Example of variables and typecasting
name = "Vaibhav"
age = 25
gpa = 7.9
print(f"My name is {name}, I am {age} years old, and my GPA is {gpa:.2f}.")

# Example of user input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(f"Hello {user_name}, you are {user_age} years old.")

# Example of arithmetic operations
a = 10
b = 5
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

# Example of using a list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Fruits:", fruits)

# Example of a loop
for fruit in fruits:
    print(fruit)

# Example of a function
def greet(person):
    return f"Hello, {person}!"

print(greet("Vaibhav"))

# Example of using the random module
import random
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")