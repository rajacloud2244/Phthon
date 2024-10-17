#A function is a reusable block of code that performs a specific task. It can take inputs (called parameters), execute some code, and often return a result.

def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0

print(is_even(4))  # Output: True
print(is_even(7))  # Output: False



"""
Def: Keyword of the function
Function Name: is_even
Parameter: num is the number to check.
Logic: The function uses the modulus operator % to check if num is divisible by 2. If it is, the function returns True (indicating the number is even); otherwise, it returns False.


"""
#Function with Default Argument Values

def greet(name, greeting="Hello"):
    """Greet a person with a given greeting."""
    print(f"{greeting}, {name}!")

# Calling the function with both arguments
greet("Alice", "Hi")  # Output: Hi, Alice!

# Calling the function with only the required argument
greet("Bob")          # Output: Hello, Bob!


"""
Parameters:

name: This is a required parameter. You must provide a value for this when calling the function.
greeting: This is an optional parameter with a default value of "Hello". If you don't provide a value for this parameter when calling the function, it will automatically use "Hello".
Docstring:

Greet a person with a given greeting.is a description of what the function does. It's not necessary for the function to work, but it's helpful for documentation.
Print Statement:

The line print(f"{greeting}, {name}!") uses an f-string to format the output. It prints the greeting followed by the name.

Function Calls

Calling with Both Arguments:

greet("Alice", "Hi")  # Output: Hi, Alice!
Here, you provide both the name and greeting.
"Alice" is assigned to name, and "Hi" is assigned to greeting.
The function prints: Hi, Alice!

Calling with Only the Required Argument:


greet("Bob")          # Output: Hello, Bob!
In this case, you only provide the name as "Bob".
Since you didn't provide a value for greeting, it uses the default value, which is "Hello".
The function prints: Hello, Bob!
Summary

"""