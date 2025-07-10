#Loops
# are an esential part of programming that allow you to repeat a block of code multiple times.

# A loop is a control structure that allows you to execute a block of code repeatedly based on a condition. 
# Python has two main types of loops: `for` loops and `while` loops.

# For Loop
# A `for` loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.

fruit = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)  # This will print each fruit in the list

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)  # This will print each number in the list

# While Loop
# A `while` loop continues to execute as long as a specified condition is true.

count = 1
while count <= 5:
    print(count)  # This will print numbers from 1 to 5
    count += 1  # Increment the count by 1 each time the loop runs

#Loop Control Statements
# break, continue, and pass are loop control statements that alter the flow of a loop.

# Break Statement
# The `break` statement is used to exit a loop prematurely when a certain condition is met.

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        break  # Exit the loop when "cherry" is found
    print(fruit)  # This will print "apple" and "banana"

# Continue Statement
# The `continue` statement skips the current iteration of a loop and moves to the next iteration.

print()
for fruit in fruits:
    if fruit == "banana":
        continue  # Skip the iteration when "banana" is found
    print(fruit)  # This will print "apple", "cherry", and "date"

# Pass Statement
# The `pass` statement is a null operation; it does nothing when executed. It is often used as a placeholder.

print()
for fruit in fruits:
    if fruit == "banana":
        pass  # Do nothing for "banana"
    print(fruit)  # This will print all fruits, including "banana"


count = 0
while count < 5:
    print(count)
    count += 1
# This will print numbers from 0 to 4
if count == 3:
    break  # This will not execute because count is now 5