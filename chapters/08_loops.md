# Contents of the file: /python-notes/python-notes/chapters/08_loops.md

# Chapter 08: Loops in Python

Loops are a fundamental concept in programming that allow you to execute a block of code repeatedly based on a condition or over a sequence of elements. In Python, there are two primary types of loops: **for loops** and **while loops**.

## 1. For Loops

A **for loop** is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. The loop executes a block of code for each item in the sequence.

### Example of a For Loop

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

In this example, the loop goes through each fruit in the `fruits` list and prints it.

## 2. While Loops

A **while loop** continues to execute a block of code as long as a specified condition is true. It is useful when the number of iterations is not known beforehand.

### Example of a While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Output:**
```
0
1
2
3
4
```

In this example, the loop prints the value of `count` until it reaches 5.

## 3. Controlling Loop Execution

You can control the execution of loops using the `break` and `continue` statements.

### Break Statement

The `break` statement is used to exit a loop prematurely when a certain condition is met.

#### Example of Break

```python
for number in range(10):
    if number == 5:
        break
    print(number)
```

**Output:**
```
0
1
2
3
4
```

### Continue Statement

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

#### Example of Continue

```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```

**Output:**
```
0
1
3
4
```

In this example, when `number` is 2, the loop skips the print statement and continues with the next iteration.

## Conclusion

Loops are essential for performing repetitive tasks efficiently in Python. Understanding how to use `for` and `while` loops, along with controlling their execution with `break` and `continue`, is crucial for effective programming.