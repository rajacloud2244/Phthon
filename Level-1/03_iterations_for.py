'''The for statement in Python is designed for iterating over items in a sequence, like lists, strings dictonary (key -value pair),rather than using numeric ranges as in some other languages. This makes it intuitive and flexible for working with collections.'''

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

'''
List Definition: words is a list containing three strings: 'cat', 'window', and 'defenestrate'.

For Loop: The loop for w in words: iterates over each item in the words list. In each iteration, the variable w takes on the value of the current word.

Print Statement: The print(w, len(w)) statement prints the current word (w) and its length (len(w)).

'''

# Sample collection of students and their grades
# define a dictinary wuth name grades (key value pair)

grades = {
    'Alice': 85,
    'Bob': 58,
    'Charlie': 72,
    'David': 45,
    'Eve': 90
}

# Strategy: Iterate over a copy
for student, grade in grades.copy().items():
    if grade < 60:
        del grades[student]

# Print the remaining students
print(grades)  # Output: {'Alice': 85, 'Charlie': 72, 'Eve': 90}


'''
grades.copy()

This method creates a shallow copy of the grades dictionary. A shallow copy means that a new dictionary is created with the same key-value pairs as the original, but it is independent of the original dictionary. Any changes made to the original grades dictionary will not affect the copied version.
.items()

The items() method is called on the copied dictionary. This method returns a view object that displays a list of the dictionary's key-value tuple pairs. In our case, it provides pairs of student names and their corresponding grades.
for student, grade in ...:

This part of the line initiates a for loop that iterates over the key-value pairs obtained from the copied dictionary.
In each iteration:
The variable student will hold the key (the name of the student).
The variable grade will hold the value (the student's grade).

'''


'''
If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

'''

for i in range(5):
    print(i)

    