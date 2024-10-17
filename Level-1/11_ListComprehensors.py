'''
What is a List Comprehension?
A list comprehension is a way to create a new list by transforming or filtering items from an existing list. Think of it as a shorthand for a for-loop that makes a new list.

Basic Concept
Starting Point: You have an existing list or a range of numbers.
Transformation: You apply an operation to each item (like squaring it).
              : You can choose to include only certain items based on a condition.

'''

# List Comprehensions Example

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Create a new list with each number doubled
doubled = [x * 2 for x in numbers]

# Print the new list
print(doubled)  # Output: [2, 4, 6, 8, 10]


#Another Example: Filtering Values
# List of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Create a new list with only even numbers
evens = [x for x in numbers if x % 2 == 0]

# Print the new list
print(evens)  # Output: [2, 4, 6]


#Nested list comprensions

# Create a 3x3 matrix
matrix = [[row * col for col in range(3)] for row in range(3)]

print(matrix)
