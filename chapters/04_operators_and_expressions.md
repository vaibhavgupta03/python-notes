# Operators and Expressions in Python

## Introduction
Operators in Python are special symbols that perform operations on variables and values. They are essential for performing calculations, comparisons, and logical operations. This chapter covers the main types of operators in Python, including arithmetic operators, comparison operators, and logical operators.

## 1. Arithmetic Operators
Arithmetic operators are used to perform mathematical operations. The basic arithmetic operators in Python are:

- **Addition (`+`)**: Adds two operands.
- **Subtraction (`-`)**: Subtracts the second operand from the first.
- **Multiplication (`*`)**: Multiplies two operands.
- **Division (`/`)**: Divides the first operand by the second (returns a float).
- **Floor Division (`//`)**: Divides the first operand by the second and returns the largest integer less than or equal to the result.
- **Modulus (`%`)**: Returns the remainder of the division of the first operand by the second.
- **Exponentiation (`**`)**: Raises the first operand to the power of the second.

### Example:
```python
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a // b) # Output: 3
print(a % b)  # Output: 1
print(a ** b) # Output: 1000
```

## 2. Comparison Operators
Comparison operators are used to compare two values. They return a Boolean value (`True` or `False`). The main comparison operators are:

- **Equal to (`==`)**: Checks if two operands are equal.
- **Not equal to (`!=`)**: Checks if two operands are not equal.
- **Greater than (`>`)**: Checks if the left operand is greater than the right.
- **Less than (`<`)**: Checks if the left operand is less than the right.
- **Greater than or equal to (`>=`)**: Checks if the left operand is greater than or equal to the right.
- **Less than or equal to (`<=`)**: Checks if the left operand is less than or equal to the right.

### Example:
```python
x = 5
y = 10

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: False
print(x < y)   # Output: True
print(x >= y)  # Output: False
print(x <= y)  # Output: True
```

## 3. Logical Operators
Logical operators are used to combine conditional statements. The main logical operators are:

- **And (`and`)**: Returns `True` if both operands are true.
- **Or (`or`)**: Returns `True` if at least one of the operands is true.
- **Not (`not`)**: Reverses the logical state of its operand.

### Example:
```python
a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False
```

## Conclusion
Understanding operators and expressions is fundamental to programming in Python. They allow you to perform calculations, make comparisons, and control the flow of your programs based on conditions. This chapter provided an overview of the primary operators available in Python, along with examples to illustrate their usage.