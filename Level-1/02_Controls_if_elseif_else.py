'''What is an if Statement?
An if statement lets your program make decisions. It checks if a condition is true or false and then runs some code based on that.

Basic Structure
Here’s how it looks in Python:

if condition:
    # Code to run if the condition is true
elif another_condition:
    # Code to run if the first condition is false and this one is true
else: (printing message)
    # Code to run if none of the conditions are true
Key Parts
if: This starts the decision-making.
elif: Short for "else if." You can have multiple elif statements to check more conditions.
else: This is optional and runs if none of the conditions above are true.


x=0 - assigment
x==0 
This is a comparison (or equality) statement.
It checks whether the value of x is equal to 0.
It returns True if x is 0 and False otherwise.


You can use an if statement to check if a number is negative and set it to zero. Here’s a simple

 '''


x = int(input("Please enter an integer: "))  # User is asked to enter a number

if x < 0:  # Check if x is less than 0
    x = 0  # If true, set x to 0
    print('Negative changed to zero')  # Print a message
elif x == 0:  # Check if x is exactly 0
    print('Zero')  # Print 'Zero' if true
elif x == 1:  # Check if x is exactly 1
    print('Single')  # Print 'Single' if true
else:  # If none of the above conditions are true
    print('More')  # Print 'More'


