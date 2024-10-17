


"""
What are Iterators?
An iterator is an object that allows you to traverse a collection, such as a list, tuple, or dictionary, one element at a time. In Python, this is typically done using a for loop
"""
# Iterating Over Collections

for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one': 1, 'two': 2}:
    print(key)

for char in "123":
    print(char)

#for line in open("myfile.txt"):
#    print(line, end='')



"""
Gnerator - similar to for loop and for each loop

While both approaches allow for iteration, generators provide additional benefits in terms of memory efficiency and can represent potentially infinite sequences. If you’re working with large datasets or need to process data on-the-fly, generators are often the better choice.





"""
def my_generator():
    for i in range(1, 6):
        yield i

for item in my_generator():
    print(item)


