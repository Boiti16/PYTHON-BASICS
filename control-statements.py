#Control Statements
# Control statements are used to control the flow of execution in a program.

#in python, we primarily use 3 types of control statements.

#if statements
# A control statement that allows the program to execute a block of code if a specified condition is true.

num = 10
if num > 0 :
    print("The number is positive.") # This block of code will execute if the condition is true.


#else statement
# A control statement that allows the program to execute a block of code if the condition in the if statement is false.

num = -1
if num > 0 :
    print("The number is positive.") # This block of code will not execute because the condition is false.
else :
    print("The number is negative.") # This block of code will execute because the condition in the if statement is false.


#elseif statement
# A control statement that allows the program to check multiple conditions. If the first condition is false, it checks the next condition, and so on.

num = -5
if num > 0 :
    print("The number is positive.") 
elif num == 0 :
    print("The number is zero.") # This block of code will execute if the condition in the if statement is false and the condition in the elif statement is true.
else :
    print("The number is negative.")