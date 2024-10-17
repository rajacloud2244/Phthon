"""
1. Output in Python
In Python, you can display output in various ways. The most common methods are:

Using the print() function.
Writing to a file.
Using the write() method of file objects.

"""

"""
2. Fancier Output Formatting
Python provides several methods for formatting output beyond simple printing.
F-strings are a way to create strings that can include variables and expressions directly inside the string. They make it easy to combine text with data.
Formatted String Literals (f-strings)
Syntax: Start a string with f or F, and use {} to include expressions.

"""
year = 2023
event = 'Conference'
print(f'Results of the {year} {event}')  # Results of the 2023 Conference



"""
Components
{:-9}:

This placeholder formats the yes_votes variable.
The : indicates that formatting options follow.
-9 means to left-align the number in a field that is 9 characters wide. If yes_votes is shorter than 9 characters, it will be padded with spaces on the right.
{:2.2%}:

This placeholder formats the percentage variable.
2.2 specifies that the output should be a percentage with 2 digits total, and 2 digits after the decimal point.
The % indicates that the value should be multiplied by 100 and displayed as a percentage.

"""


#Using str.format() Method
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
# Output: ' 42572654 YES votes  49.67%'

#String Formatting Options
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

""" Using str() and repr()
str(): For human-readable representations.
repr(): For representations that can be read by the interpreter."""
s = 'Hello, world.'
print(str(s))  # Hello, world.
print(repr(s)) # 'Hello, world.'


#Advanced Formatting with str.format()

print('{0} and {1}'.format('spam', 'eggs'))  # Positional Arguments- spam and eggs

print('This {food} is {adjective}.'.format(food='spam', adjective='horrible')) # Keyword Arguments

#Creating Aligned Tables

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

