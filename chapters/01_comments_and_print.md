# Chapter 01: Comments and Print

## Comments in Python

Comments are used in Python to explain code and make it more readable. They are ignored by the interpreter, meaning they do not affect the execution of the program. Comments can be single-line or multi-line.

### Single-line Comments

Single-line comments start with the `#` symbol. Everything following the `#` on that line will be treated as a comment.

**Example:**
```python
# This is a single-line comment
print("Hello, World!")  # This prints a message to the console
```

### Multi-line Comments

Multi-line comments can be created using triple quotes (`"""` or `'''`). This allows you to write comments that span multiple lines.

**Example:**
```python
"""
This is a multi-line comment.
It can span multiple lines.
"""
print("This will be printed.")
```

## The Print Function

The `print()` function is used to output text or variables to the console. It can take multiple arguments and can format the output in various ways.

### Basic Usage

**Example:**
```python
print("Hello, World!")  # Outputs: Hello, World!
```

### Printing Variables

You can also print variables by passing them to the `print()` function.

**Example:**
```python
name = "Vaibhav"
age = 21
print(name, age)  # Outputs: Vaibhav 21
```

### Formatting Output

You can format the output using f-strings or the `format()` method.

**Example with f-strings:**
```python
print(f"My name is {name} and I am {age} years old.")  # Outputs: My name is Vaibhav and I am 25 years old.
```

**Example with format():**
```python
print("My name is {} and I am {} years old.".format(name, age))  # Outputs: My name is Vaibhav and I am 25 years old.
```

## Conclusion

In this chapter, we covered the importance of comments in Python for code documentation and readability. We also explored the `print()` function, which is essential for outputting information to the console. Understanding how to use comments and the print function is fundamental for writing clear and effective Python code.