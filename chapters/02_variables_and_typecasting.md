# Variables and Typecasting in Python

## Introduction to Variables
In Python, a variable is a reserved memory location used to store values. Variables allow you to label data and use it throughout your program. You can think of a variable as a container that holds information.

### Example:
```python
first_name = "Vaibhav"  # A variable that stores a string
age = 21  # A variable that stores an integer
gpa = 8.9  # A variable that stores a float
```

## Naming Variables
When naming variables, you should follow these rules:
- Variable names can contain letters, numbers, and underscores.
- They must start with a letter or an underscore.
- Variable names are case-sensitive (e.g., `age` and `Age` are different variables).
- Avoid using reserved keywords (e.g., `if`, `else`, `while`, etc.).

### Example:
```python
user_name = "Vaibhav"  # Valid variable name
user1 = "Vaibhav"  # Valid variable name
1st_user = "Vaibhav"  # Invalid variable name (cannot start with a number)
```

## Typecasting
Typecasting is the process of converting one data type into another. In Python, you can use built-in functions to perform typecasting. The most common typecasting functions are:
- `str()`: Converts a value to a string.
- `int()`: Converts a value to an integer.
- `float()`: Converts a value to a float.

### Example:
```python
age = 21  # Integer
age_str = str(age)  # Convert integer to string
print(age_str)  # Output: "21"

gpa = 8.9  # Float
gpa_int = int(gpa)  # Convert float to integer
print(gpa_int)  # Output: 8

is_student = True  # Boolean
is_student_str = str(is_student)  # Convert boolean to string
print(is_student_str)  # Output: "True"
```

## Conclusion
Understanding variables and typecasting is fundamental in Python programming. Variables allow you to store and manipulate data, while typecasting enables you to convert data types as needed. By mastering these concepts, you can write more flexible and dynamic Python code.