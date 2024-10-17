"""
Errors in Python can be categorized mainly into two types: syntax errors and exceptions.

Syntax Errors
Syntax errors, or parsing errors, occur when the code is not correctly structured according to the Python language rules. For instance:
"""

# while True print('Hello world') - uncomment for  practise

#Exceptions:-Exceptions are errors detected during the execution of the code, even if the syntax is correct. For example:
# 10 * (1/0) -  - uncomment for  practise
"""
Other types of exceptions include:

NameError: when a variable is not defined.
TypeError: when an operation or function is applied to an object of inappropriate type. """

"""
Handling Exceptions

Python provides a way to handle exceptions using try and except blocks. Here’s an example that repeatedly asks for valid integer input:

"""
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")


"""
If the code in the try block executes without raising an exception, the except block is skipped. If an exception occurs, the corresponding except block will be executed.

You can define yours own exceptions i,e user defined exceptions

"""