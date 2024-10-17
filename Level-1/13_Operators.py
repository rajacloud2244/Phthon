"""
1. Comparison Operators
Comparison operators allow you to compare values and return Boolean results (True or False).

Equality and Inequality:

== : Equals
!= : Not equal
Greater than and Less than:

> : Greater than
< : Less than
>= : Greater than or equal to
<= : Less than or equal to
2. Membership Tests
Membership tests check for the presence of a value in a container (like a list, tuple, or string).

Membership Operators:
in : Returns True if the value is found in the container.
not in : Returns True if the value is not found in the container.

3. Identity Operators
Identity operators compare whether two variables point to the same object in memory.

Identity Operators:
is : Returns True if both variables point to the same object.
is not : Returns True if both variables point to different objects.

4. Chaining Comparisons
Chaining comparisons allows you to combine multiple comparisons in a single expression.

5. Boolean Operators
Boolean operators combine multiple conditions.

Boolean Operators:
and : True if both operands are true.
or : True if at least one operand is true.
not : Inverts the Boolean value of the operand.

6. Short-Circuit Evaluation
Short-circuit evaluation refers to how Python evaluates Boolean expressions:

In and operations, if the first operand is False, the second operand is not evaluated.
In or operations, if the first operand is True, the second operand is not evaluated.

7. Walrus Operator
The walrus operator (:=) allows assignment within expressions, introduced in Python 3.8.

"""

# Comparison Operators
a = 5
b = 10

print("Comparison Operators:")
print(f"a < b: {a < b}")  # True
print(f"a == b: {a == b}")  # False
print(f"a != b: {a != b}")  # True
print(f"a > b: {a > b}")  # False
print(f"a <= b: {a <= b}")  # True
print(f"a >= b: {a >= b}")  # False
print()

# Membership Tests
my_list = [1, 2, 3, 4, 5]

print("Membership Tests:")
print(f"3 in my_list: {3 in my_list}")  # True
print(f"6 not in my_list: {6 not in my_list}")  # True
print()

# Identity Operators
list1 = [1, 2, 3]
list2 = list1  # Same object
list3 = list1[:]  # Copy of list1

print("Identity Operators:")
print(f"list1 is list2: {list1 is list2}")  # True
print(f"list1 is list3: {list1 is list3}")  # False
print()

# Chaining Comparisons
x = 5
print("Chaining Comparisons:")
print(f"2 < x < 10: {2 < x < 10}")  # True
print()

# Boolean Operators
print("Boolean Operators:")
print(f"x < 10 and b > 5: {x < 10 and b > 5}")  # True
print(f"x > 10 or b > 5: {x > 10 or b > 5}")  # True
print(f"not (x < 10): {not (x < 10)}")  # False
print()

# Short-Circuit Evaluation
a = True
b = False
c = True

print("Short-Circuit Evaluation:")
result = a and b and c  # Stops at b
print(f"Result of a and b and c: {result}")  # False
print()

# Assignment with the Walrus Operator
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3

print("Walrus Operator:")
print(f"First non-null string: {non_null}")  # 'Trondheim'

# Using the walrus operator in an expression
if (n := len(non_null)) > 0:
    print(f"Length of non_null is {n}.")  # Length of non_null is 9
