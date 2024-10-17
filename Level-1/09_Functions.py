"""
Arbitrary argument lists in Python allow functions to accept a variable number of positional arguments using *args (treated as a tuple)

Keyword arguments using **kwargs (treated as a dictionary). 

This flexibility enhances code reusability and simplifies function definitions for varying input scenarios.

"""
def describe_fruits(*fruits, **nutritional_info):
    print("Fruits:", fruits)
    for fruit, info in nutritional_info.items():
        print(f"{fruit}: {info}")

#fruit is a variable that holds the keys of the nutritional_info dictionary (like "vitamin_c" and "fiber"). It allows you to access and display the corresponding values

#info is a variable that represents the value associated with each key in the nutritional_info dictionary.

# Calling the function
describe_fruits("apple", "banana", vitamin_c="high", fiber="medium")

# fruits - tuple
# nutritional_info -dictionary



"""
def function_name(param1: type1, param2: type2) -> return_type:
    # function body


Explanation
x: int and y: int indicate that both parameters are expected to be integers.
-> int signifies that the function will return an integer.
Notes
Annotations can be any expression, not just types. For instance, you can use strings or other objects.
Annotations do not affect how the function behaves; they are mainly for documentation purposes and can be accessed via the __annotations__ attribute of the function.

"""

def add(x: int, y: int) -> int:
    """Return the sum of x and y."""
    return x + y

# Calling the function
result = add(3, 5)
print(result)  # Output: 8
