

#The del statement in Python is used to delete objects. This can include variables, list items, or even entire lists.
numbers = [1, 2, 3, 4, 5]
del numbers[2]  # Delete the item at index 2 (which is 3)
print(numbers)  # Output: [1, 2, 4, 5]

#A tuple is a collection of items that is ordered and immutable (cannot be changed). Tuples are defined using parentheses ().

my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
print(my_tuple[0])  # Output: 1
# my_tuple[0] = 10  # This would raise a TypeError

#Sets- A set is an unordered collection of unique items. Sets are defined using curly braces {}.
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set.add(6)  # Add an item
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)  # Remove an item
print(my_set)  # Output: {1, 2, 4, 5, 6}


#Dictionary-A dictionary is a collection of key-value pairs. Dictionaries are unordered and mutable, defined using curly braces {} with keys and values separated by a colon :.

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25}

print(my_dict['name'])  # Output: Alice


