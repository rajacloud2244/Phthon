'''
break to exit a loop when a condition is met.

Use continue to skip the current iteration and move to the next one.

'''

for num in range(5):
    if num == 3: # We won't break, so this condition is ignored
        pass  # Just a placeholder; no action taken - instead of if logical statemets
    print(num)

# with break
for num in range(5):
    if num == 3:
        break  # Exit the loop when num is 3
    print(num)

#with continue
for num in range(5):
    if num == 2:

        continue  # Skip the rest of the loop when num is 2
    print(num)

#skips the 2nd iteration in the loop

