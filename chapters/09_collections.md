# Collections in Python

Collections in Python are data structures that allow you to store multiple values in a single variable. The main types of collections in Python include:

## 1. Lists
- **Definition**: Lists are ordered, changeable, and allow duplicate values. They are defined using square brackets `[]`.
- **Example**:
  ```python
  fruits = ["apple", "banana", "cherry", "mango"]
  print(fruits)  # Output: ['apple', 'banana', 'cherry', 'mango']
  ```
- **Common Operations**:
  - Adding elements: `fruits.append("orange")`
  - Inserting elements: `fruits.insert(1, "kiwi")`
  - Removing elements: `fruits.remove("banana")`
  - Accessing elements: `print(fruits[0])  # Output: apple`

## 2. Tuples
- **Definition**: Tuples are ordered, unchangeable (immutable), and allow duplicate values. They are defined using parentheses `()`.
- **Example**:
  ```python
  car_tuple = ("BMW", "Audi", "Mercedes")
  print(car_tuple)  # Output: ('BMW', 'Audi', 'Mercedes')
  ```
- **Common Operations**:
  - Accessing elements: `print(car_tuple[1])  # Output: Audi`
  - Counting occurrences: `print(car_tuple.count("BMW"))  # Output: 1`

## 3. Sets
- **Definition**: Sets are unordered, unchangeable, and do not allow duplicate values. They are defined using curly braces `{}`.
- **Example**:
  ```python
  cars = {"BMW", "Audi", "Mercedes"}
  print(cars)  # Output: {'BMW', 'Audi', 'Mercedes'}
  ```
- **Common Operations**:
  - Adding elements: `cars.add("Toyota")`
  - Removing elements: `cars.remove("Audi")`
  - Checking membership: `"BMW" in cars  # Output: True`

## 4. Dictionaries
- **Definition**: Dictionaries are unordered, changeable, and consist of key-value pairs. They are defined using curly braces `{}` with a colon `:` separating keys and values.
- **Example**:
  ```python
  capitals = {
      "India": "New Delhi",
      "USA": "Washington D.C.",
      "Japan": "Tokyo"
  }
  print(capitals["India"])  # Output: New Delhi
  ```
- **Common Operations**:
  - Adding key-value pairs: `capitals["France"] = "Paris"`
  - Removing key-value pairs: `capitals.pop("Japan")`
  - Accessing values: `print(capitals.get("USA"))  # Output: Washington D.C.`

## Summary
Collections in Python provide versatile ways to store and manipulate data. Understanding how to use lists, tuples, sets, and dictionaries is essential for effective programming in Python. Each collection type has its own characteristics and use cases, making them suitable for different scenarios.