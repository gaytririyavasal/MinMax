PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Write a program in file MinMax.py that accepts an arbitrary number of integer inputs from the user and prints out the count of numbers entered, the minimum and maximum of the numbers entered. The user will end the input loop by typing in the string 'stop'. When the user enters 'stop' your program should print out a blank line, the count of numbers entered, the minimum integer entered and the maximum integer entered. If the user enters 'stop' immediately (i.e., before any numbers are entered), you'll print a slightly different message. See the examples below.

You can assume that the values entered are integers (positive, negative or zero) or the string 'stop' (lowercase). You don't have to validate the inputs. Everything is separated by a single space.

Remember that all input arrives as strings. So you have to check whether it's the string 'stop' before you convert it to an integer.

Below is some sample output. You should mimic this exactly for the given inputs.

> python MinMax.py
Enter an integer or 'stop' to end: stop

You didn't enter any numbers
> python MinMax.py
Enter an integer or 'stop' to end: 87
Enter an integer or 'stop' to end: stop

You entered 1 numbers
The maximum is 87
The minimum is 87
> python MinMax.py
Enter an integer or 'stop' to end: -10
Enter an integer or 'stop' to end: 0
Enter an integer or 'stop' to end: +42
Enter an integer or 'stop' to end: 87
Enter an integer or 'stop' to end: -100
Enter an integer or 'stop' to end: stop

You entered 5 numbers
The maximum is 87
The minimum is -100
>

This homework is designed to give you some practice using loops.

Notice that we haven't yet covered lists in the class, so don't use them. But you don't need them. Think about this problem as follows. Suppose we're talking and I tell you I'm going to rattle off a bunch of numbers. At the end, I want you to tell me the biggest number I mentioned. I start: "9, 15, 130, 2, 14, ...." Notice that you certainly don't need to remember all of the numbers. At any point, you only need to remember the biggest number I've mentioned to that point. If you hear a smaller number, you ignore it. But if you hear a bigger number, then that's the new biggest number so far and you just need to remember that one.
