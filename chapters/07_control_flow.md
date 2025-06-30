# Control Flow in Python

Control flow statements in Python allow you to execute certain blocks of code based on specific conditions. This chapter covers the primary control flow statements: `if`, `elif`, and `else`.

## 1. If Statement

The `if` statement is used to test a condition. If the condition evaluates to `True`, the block of code within the `if` statement is executed.

### Example:
```python
age = 18
if age >= 18:
    print("You are an adult.")
```
In this example, since `age` is 18, the output will be:
```
You are an adult.
```

## 2. Elif Statement

The `elif` (short for "else if") statement allows you to check multiple expressions for `True` and execute a block of code as soon as one of the conditions is `True`.

### Example:
```python
age = 16
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```
In this case, the output will be:
```
You are a teenager.
```

## 3. Else Statement

The `else` statement is used to execute a block of code when none of the preceding conditions are `True`.

### Example:
```python
age = 10
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```
Here, the output will be:
```
You are a child.
```

## 4. Nested If Statements

You can also nest `if` statements within each other to check multiple conditions.

### Example:
```python
age = 20
if age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You can drink alcohol.")
else:
    print("You are not an adult.")
```
In this example, the output will be:
```
You are an adult.
You can drink alcohol.
```

## 5. Conclusion

Control flow statements are essential for making decisions in your code. By using `if`, `elif`, and `else`, you can control the execution of your program based on different conditions, allowing for more dynamic and responsive code.