## Fstrings: The expressions are evaluated at runtime and formatted using the specified format.
#Function with Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")  #Using f-string
    print(f"My {animal_type}'s name is {pet_name}.") #Using f-string

# Calling the function using positional arguments
describe_pet('hamster', 'Harry')  
# Output: 
# I have a hamster.
# My hamster's name is Harry.

# Calling the function using keyword arguments
describe_pet(animal_type='dog', pet_name='Rex')
# Output: 
# I have a dog.
# My dog's name is Rex.



"""
What is a Lambda Function?
A lambda function is a way to create small, unnamed functions in Python. You use the lambda keyword to define it.

Key Points
Anonymous: Lambda functions don’t have a name like regular functions defined with def.

Single Expression: They can only perform one operation. You can't write multiple lines of code inside a lambda.

Return Value: They automatically return the result of their single expression.

When to Use Lambda Functions
Quick Operations: When you need a simple function for a short period and don’t want to write a full function.

Functional Programming: When you’re using functions like map, filter, or sorted.

"""


# Define a lambda function to add two numbers
add = lambda x, y: x + y
#lambda arguments: expression

# Use the lambda function
result = add(3, 5)  # This will add 3 and 5
print(result)  # Output: 8


"""
lambda: The keyword that signifies the start of the lambda function.
arguments: A comma-separated list of parameters (like in a normal function).
expression: A single expression that the function evaluates and returns.
"""