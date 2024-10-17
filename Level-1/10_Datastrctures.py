

fruits = ['apple', 'banana']

# 1. append() #add
fruits.append('orange')
print("After append:", fruits)  # Output: ['apple', 'banana', 'orange']

# 2. extend()
fruits.extend(['kiwi', 'mango'])
print("After extend:", fruits)  # Output: ['apple', 'banana', 'orange', 'kiwi', 'mango']

# 3. insert()
fruits.insert(1, 'grape')
print("After insert:", fruits)  # Output: ['apple', 'grape', 'banana', 'orange', 'kiwi', 'mango']

# 4. remove()
fruits.remove('banana')
print("After remove:", fruits)  # Output: ['apple', 'grape', 'orange', 'kiwi', 'mango']

# 5. pop()
last_fruit = fruits.pop()
print("Popped fruit:", last_fruit)  # Output: mango
print("After pop:", fruits)          # Output: ['apple', 'grape', 'orange', 'kiwi']

# 6. clear()
fruits.clear()
print("After clear:", fruits)  # Output: []

# 7. index()
fruits = ['apple', 'grape', 'orange']
index_of_grape = fruits.index('grape')
print("Index of grape:", index_of_grape)  # Output: 1

# 8. count()
fruits.append('apple')
count_of_apples = fruits.count('apple')
print("Count of apples:", count_of_apples)  # Output: 2

# 9. sort()
fruits.sort(reverse=True)
print("After sort:", fruits)  # Output: ['orange', 'grape', 'apple', 'apple']

# 10. reverse()
fruits.reverse()
print("After reverse:", fruits)  # Output: ['apple', 'apple', 'grape', 'orange']

# 11. copy()
fruits_copy = fruits.copy()
print("Copy of fruits:", fruits_copy)  # Output: ['apple', 'apple', 'grape', 'orange']



"""
Here's a concise summary of all the list methods in Python:

1. **`append(x)`**: Adds an item `x` to the end of the list.
2. **`extend(iterable)`**: Extends the list by appending all items from the iterable.
3. **`insert(i, x)`**: Inserts item `x` at position `i`.
4. **`remove(x)`**: Removes the first item with value `x`. Raises `ValueError` if not found.
5. **`pop([i])`**: Removes and returns the item at position `i`. If no index is specified, removes the last item.
6. **`clear()`**: Removes all items from the list.
7. **`index(x[, start[, end]])`**: Returns the index of the first item with value `x`. Raises `ValueError` if not found.
8. **`count(x)`**: Returns the number of times `x` appears in the list.
9. **`sort(*, key=None, reverse=False)`**: Sorts the items of the list in place.
10. **`reverse()`**: Reverses the elements of the list in place.
11. **`copy()`**: Returns a shallow copy of the list.

This encapsulates the key functionalities of the list data type in Python.
"""


# Ques- first in first out
from collections import deque #module

# Initialize the queue with some elements
queue = deque(["Eric", "John", "Michael"])

#deque- It's a special kind of list that lets you add or remove items from both ends very quickly.

# Adding elements to the queue
queue.append("Terry")   # Terry arrives
queue.append("Graham")  # Graham arrives

# Removing elements from the queue (FIFO order)
first_out = queue.popleft()  # The first to arrive leaves
print(f'{first_out} has left the queue.')  # Output: Eric has left the queue.

second_out = queue.popleft()  # The second to arrive leaves
print(f'{second_out} has left the queue.')  # Output: John has left the queue.

# Display the remaining elements in the queue
print(f'Remaining queue: {queue}')  # Output: Remaining queue: deque(['Michael', 'Terry', 'Graham'])



#For stacks first in last out

from collections import deque

# Create a new deque to use as a stack
stack = deque()

# Add items to the stack
stack.append("A")  # Stack: deque(['A'])
stack.append("B")  # Stack: deque(['A', 'B'])
stack.append("C")  # Stack: deque(['A', 'B', 'C'])

# Remove items from the stack
print(stack.pop())  # Output: 'C' (last added)
print(stack.pop())  # Output: 'B' (next last added)

# Final state of the stack
print(stack)        # Output: deque(['A'])
