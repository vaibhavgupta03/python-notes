# Contents of the file: /python-notes/python-notes/chapters/14_args_kwargs.md

# Chapter 14: Arbitrary Arguments in Functions

In Python, functions can accept a variable number of arguments. This is useful when you want to create functions that can handle different amounts of input. There are two main ways to achieve this: using `*args` and `**kwargs`.

## 1. Using *args

The `*args` syntax allows you to pass a variable number of non-keyword arguments to a function. The arguments are received as a tuple within the function.

### Example:

```python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15
```

In this example, the `add_numbers` function can accept any number of arguments. The `args` parameter collects all the arguments into a tuple, which we then iterate over to calculate the total.

## 2. Using **kwargs

The `**kwargs` syntax allows you to pass a variable number of keyword arguments to a function. The arguments are received as a dictionary within the function.

### Example:

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Vaibhav", age=21, city="New York")
```

In this example, the `display_info` function can accept any number of keyword arguments. The `kwargs` parameter collects all the keyword arguments into a dictionary, which we then iterate over to print each key-value pair.

## 3. Combining *args and **kwargs

You can also combine `*args` and `**kwargs` in a single function definition. When doing so, `*args` must come before `**kwargs`.

### Example:

```python
def mixed_arguments(arg1, *args, **kwargs):
    print(f"First argument: {arg1}")
    print("Additional arguments:", args)
    print("Keyword arguments:", kwargs)

mixed_arguments(10, 20, 30, name="Vaibhav", age=21)
```

In this example, the `mixed_arguments` function takes one regular argument (`arg1`), a variable number of additional arguments (`*args`), and a variable number of keyword arguments (`**kwargs`). The output will show how each type of argument is handled.

## Conclusion

Using `*args` and `**kwargs` allows for greater flexibility in function definitions, enabling you to create functions that can handle a variety of input scenarios. This is particularly useful in cases where the number of inputs may vary or when you want to provide additional options through keyword arguments.