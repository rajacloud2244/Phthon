"""
Modules
Definition: A module is a file containing Python definitions (functions, variables, classes) and statements. The filename is the module name with a .py extension.

Purpose:

To organize code into separate files for easier maintenance and readability.
To reuse functions or variables across multiple scripts without duplicating code.

Creating a Module:

Use a text editor to create a Python file (e.g., fibo.py).
Define functions or variables in this file.

Example Functions:

A function to print Fibonacci numbers up to a specified limit.
A function to return Fibonacci numbers as a list.

Using a Module:

Import the module using the import statement.
Access the functions using the module name followed by a dot.

Packages in Python

Definition:

Packages are a way to organize Python’s module namespace using "dotted module names". For example, A.B refers to a submodule B within a package A.
Purpose:

Packages prevent naming conflicts by allowing different modules to have the same name as long as they are in different packages.


Below is example for understanding modules

sound/                          # Top-level package
      __init__.py               # Initialize the sound package
      formats/                  # Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
      effects/                  # Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
      filters/                  # Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py

              
Importing a Submodule
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)


Importing with Alias
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)


Directly Importing a Function:
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)


              """


#Dir Function - The dir() function in Python is used to see what names (like functions, variables, classes) are defined in a module. Think of it as a way to get a list of everything you can use from that module.


import math

# Get the list of names defined in the math module
math_names = dir(math)
print(math_names)


