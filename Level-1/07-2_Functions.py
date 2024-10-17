"""
When to Use Each Type
Positional-only: Use this when you want to enforce the order of arguments or when the names don't add meaning.
Keyword-only: Use this for clarity, especially when the meaning of the arguments is important.
The / indicates that the parameters before it must be positional-only. The * indicates that parameters after it must be keyword-only.
"""

# Function Parameter Types Overview

def positional_only(param1, param2, /):
    """This function uses positional-only parameters."""
    return param1 + param2

def positional_or_keyword(param1, param2):
    """This function accepts both positional and keyword parameters."""
    return param1 + param2

def keyword_only(*, param1, param2):
    """This function uses keyword-only parameters."""
    return param1 + param2

# Examples of calling the functions

# Calling positional-only parameters
result1 = positional_only(5, 10)  # Works: result1 = 15
print(f"Positional Only Result: {result1}")

# Calling positional or keyword parameters
result2 = positional_or_keyword(5, 10)  # Works: result2 = 15
print(f"Positional or Keyword Result: {result2}")

result3 = positional_or_keyword(param1=5, param2=10)  # Also works: result3 = 15
print(f"Positional or Keyword Result with Keywords: {result3}")

# Calling keyword-only parameters
result4 = keyword_only(param1=5, param2=10)  # Works: result4 = 15
print(f"Keyword Only Result: {result4}")

# Uncommenting the following line would raise a TypeError
# result5 = keyword_only(5, 10)  # This would raise a TypeError

# Example of a function with all three types
def mixed_function(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    """A function with positional-only, positional-or-keyword, and keyword-only parameters."""
    return (pos1 + pos2) * pos_or_kwd + kwd1 + kwd2

# Example of calling mixed_function
result6 = mixed_function(1, 2, 3, kwd1=4, kwd2=5)  # Works
print(f"Mixed Function Result: {result6}")

# Uncommenting the following line would raise a TypeError
# result7 = mixed_function(1, 2, kwd1=4, kwd2=5)  # This would raise a TypeError
