# Dictionaries in Python

## Definition
Dictionaries in Python are collections of key-value pairs. They are unordered, changeable, and do not allow duplicate keys. Each key must be unique and is used to access its corresponding value.

## Creating a Dictionary
You can create a dictionary using curly braces `{}` or the `dict()` function. Here’s an example:

```python
# Using curly braces
capitals = {
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "Japan": "Tokyo"
}

# Using dict() function
capitals = dict(India="New Delhi", USA="Washington D.C.", Japan="Tokyo")
```

## Accessing Values
You can access the values in a dictionary by using their corresponding keys:

```python
print(capitals["India"])  # Output: New Delhi
```

## Adding and Updating Entries
You can add new key-value pairs or update existing ones:

```python
capitals["France"] = "Paris"  # Adding a new entry
capitals["USA"] = "Washington"  # Updating an existing entry
```

## Removing Entries
You can remove entries from a dictionary using the `pop()` method or the `del` statement:

```python
capitals.pop("Japan")  # Removes the entry for Japan
del capitals["USA"]  # Deletes the entry for USA
```

## Dictionary Methods
Dictionaries come with several built-in methods:

- `get(key, default)`: Returns the value for the specified key. If the key does not exist, it returns the default value.
  
  ```python
  print(capitals.get("Germany", "Not Found"))  # Output: Not Found
  ```

- `keys()`: Returns a view object that displays a list of all the keys in the dictionary.

  ```python
  print(capitals.keys())  # Output: dict_keys(['India', 'France'])
  ```

- `values()`: Returns a view object that displays a list of all the values in the dictionary.

  ```python
  print(capitals.values())  # Output: dict_values(['New Delhi', 'Paris'])
  ```

- `items()`: Returns a view object that displays a list of a dictionary's key-value tuple pairs.

  ```python
  print(capitals.items())  # Output: dict_items([('India', 'New Delhi'), ('France', 'Paris')])
  ```

## Example
Here’s a complete example demonstrating the creation, manipulation, and access of a dictionary:

```python
# Creating a dictionary
capitals = {
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "Japan": "Tokyo"
}

# Accessing a value
print(capitals["India"])  # Output: New Delhi

# Adding a new entry
capitals["France"] = "Paris"

# Updating an existing entry
capitals["USA"] = "Washington"

# Removing an entry
capitals.pop("Japan")

# Displaying all keys and values
print(capitals.keys())  # Output: dict_keys(['India', 'USA', 'France'])
print(capitals.values())  # Output: dict_values(['New Delhi', 'Washington', 'Paris'])
```

## Conclusion
Dictionaries are a powerful and flexible way to store and manage data in Python. They allow for quick access to values based on unique keys, making them ideal for various applications such as data storage, configuration settings, and more.