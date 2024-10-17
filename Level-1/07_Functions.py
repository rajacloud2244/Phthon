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

# Calling positional or keyword parameters
result2 = positional_or_keyword(5, 10)  # Works: result2 = 15
result3 = positional_or_keyword(param1=5, param2=10)  # Also works: result3 = 15

# Calling keyword-only parameters
result4 = keyword_only(param1=5, param2=10)  # Works: result4 = 15
# result5 = keyword_only(5, 10)  # This would raise a TypeError

# Recap on when to use each type:
"""
- Use positional-only when:
  - The order matters.
  - Parameter names don't add clarity.
  
- Use positional or keyword when:
  - Flexibility in calling the function is needed.

- Use keyword-only when:
  - Names provide clarity.
  - You want to avoid confusion about argument order.
"""

# Example of a function with all three types:
def mixed_function(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    """A function with positional-only, positional-or-keyword, and keyword-only parameters."""
    return (pos1 + pos2) * pos_or_kwd + kwd1 + kwd2

# Example of calling mixed_function
result6 = mixed_function(1, 2, 3, kwd1=4, kwd2=5)  # Works
# result7 = mixed_function(1, 2, kwd1=4, kwd2=5)  # This would raise a TypeError
