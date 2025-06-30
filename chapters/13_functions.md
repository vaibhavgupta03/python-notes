# Functions in Python

## Definition
Functions in Python are reusable blocks of code that perform a specific task. They help in organizing code, making it more modular and easier to maintain. Functions can take inputs, known as parameters, and can return outputs.

## Defining a Function
To define a function, use the `def` keyword followed by the function name and parentheses. Any parameters should be included within the parentheses.

### Example:
```python
def greet(name):
    print(f"Hello, {name}!")
```
In this example, the function `greet` takes one parameter, `name`, and prints a greeting message.

## Calling a Function
Once a function is defined, you can call it by using its name followed by parentheses, passing any required arguments.

### Example:
```python
greet("Vaibhav")  # Output: Hello, Vaibhav!
```

## Return Statement
Functions can return values using the `return` statement. This allows you to send back a result to the caller.

### Example:
```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result)  # Output: 15
```

## Default Arguments
You can define default values for parameters in a function. If no value is provided for that parameter when the function is called, the default value is used.

### Example:
```python
def count(start, end=10):
    for i in range(start, end):
        print(i, end=" ")
    print()

count(0)  # Output: 0 1 2 3 4 5 6 7 8 9
count(5, 15)  # Output: 5 6 7 8 9 10 11 12 13 14
```

## Keyword Arguments
Keyword arguments allow you to specify arguments by name, making the function calls more readable and allowing you to pass arguments in any order.

### Example:
```python
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

display_info(age=21, city="New York", name="Vaibhav")
```

## Arbitrary Arguments
You can use `*args` and `**kwargs` to allow a function to accept a variable number of arguments.

- `*args` allows you to pass a variable number of non-keyword arguments.
- `**kwargs` allows you to pass a variable number of keyword arguments.

### Example:
```python
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info("Vaibhav", 21, city="New York")
# Output: 
# Positional arguments: ('Vaibhav', 21)
# Keyword arguments: {'city': 'New York'}

```
```python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15
```

## Conclusion
Functions are a fundamental part of Python programming, enabling code reuse and organization. Understanding how to define, call, and manage functions is essential for writing efficient and maintainable code.