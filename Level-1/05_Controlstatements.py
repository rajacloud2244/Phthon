"""
The pass statement in Python is a placeholder that does nothing. It can be useful in several situations where syntactically something is required, but you don’t want to implement any functionality yet. Let’s go through the examples you provided in detail
"""
def placeholder_function():
    pass  # TODO: Implement this function later

class MyEmptyClass:
    pass  # Placeholder for a future class implementation


"""
 It provides a way to compare a value against multiple patterns and execute code based on which pattern matches. This feature makes it easier to handle complex conditions compared to traditional if-elif statements.
"""

# with if elseif

def describe_status(code):
    if code == 200:
        return "OK"
    elif code == 404:
        return "Not Found"
    elif code == 500:
        return "Internal Server Error"
    else:
        return "Unknown Status"

# Test the function
print(describe_status(200))  # Output: OK
print(describe_status(404))  # Output: Not Found
print(describe_status(500))  # Output: Internal Server Error
print(describe_status(999))  # Output: Unknown Status

def describe_status(code):
    match code:
        case 200:
            return "OK2"
        case 404:
            return "Not Found2"
        case 500:
            return "Internal Server Error2"
        case _: #Wildcards: The underscore _ acts as a wildcard, matching anything not caught by previous cases.
            return "Unknown Status2"

# Test the function
print(describe_status(200))  # Output: OK
print(describe_status(404))  # Output: Not Found
print(describe_status(500))  # Output: Internal Server Error
print(describe_status(999))  # Output: Unknown Status

"""
Combining Cases: You can group multiple patterns using the | operator:
case 401 | 403 | 404:
    return "Not allowed"

Variable Binding: Patterns can bind variables, allowing you to extract values directly:

"""
# vb binding example
point = (1, 2)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
