"""
Classes in Python
What is a Class?

A class is a blueprint for creating objects. It bundles data (attributes) and functionality (methods) together.
Why Use Classes?

Classes allow you to create new types of objects, which can help organize your code and model real-world things.
Key Concepts
Attributes and Methods:

Attributes: These are like variables that belong to a class or an instance of a class. For example, in a Car class, attributes could be color or model.
Methods: These are functions defined inside a class. They describe the behaviors of an object. For example, a drive method in a Car class might define how the car moves."""


class Car:
    def __init__(self, color, model):
        self.color = color  # Attribute
        self.model = model  # Attribute

    def drive(self):  # Method
        print("The car is driving.")

# Creating an instance of the Car class
my_car = Car("red", "Toyota")
print(my_car.color)  # Accessing the attribute
my_car.drive()  # Calling a method


"""
Scope and Namespaces

Namespace:

A namespace is a container where names (like variable names) are mapped to objects. For example, each module has its own namespace.

Scope:

Scope refers to the visibility of variables. In Python, there are several scopes:
Local: Inside a function or method.
Global: Outside all functions, usually at the module level.
Built-in: Contains built-in functions like print().

"""

spam = "global spam"

def scope_test():
    spam = "local spam"  # This is local to the function
    print(spam)  # Prints "local spam"

scope_test()
print(spam)  # Prints "global spam"
