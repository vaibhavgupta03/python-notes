# User Input in Python

User input is a fundamental aspect of programming that allows a program to interact with users by receiving data from them. In Python, the `input()` function is used to take input from the user. This function prompts the user for input and returns it as a string.

## Using the `input()` Function

The `input()` function can be used to display a prompt message to the user. The syntax is as follows:

```python
user_input = input("Enter your data: ")
```

### Example 1: Basic User Input

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

In this example, the program prompts the user to enter their name and then greets them with a message.

### Example 2: Converting User Input

Since the `input()` function returns data as a string, you may need to convert it to the appropriate data type for further processing. Common conversions include `int()` for integers and `float()` for floating-point numbers.

```python
age = input("Enter your age: ")
age = int(age)  # Convert the input to an integer
print(f"You are {age} years old.")
```

In this example, the user's age is taken as input and converted from a string to an integer before being used in the program.

### Example 3: Handling User Input with Typecasting

You can also combine user input with typecasting in a single line:

```python
gpa = float(input("Enter your GPA: "))  # Convert the input to a float
print(f"Your GPA is {gpa:.2f}.")  # Display the GPA with two decimal places
```

This example demonstrates how to take a floating-point number as input and format it for output.

## Summary

The `input()` function is a powerful tool for gathering user input in Python. By converting the input to the appropriate data type, you can effectively utilize the data provided by users in your programs.