# File: MinMax.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 09/27/2021
# Date Last Modified: 10/1/2021
# Description of Program: The following program will return the maximum and minimum of all numbers entered.

def main () :
    c = 0

    while (True):
        i = input("Enter an integer or 'stop' to end: ")
        if i == "stop" and c == 0:
            print("You didn't enter any numbers")
            break
        elif i == "stop":
            print("The maximum is", maximum)
            print("The minimum is", minimum)
            break
        elif c == 0:
            minimum = int(i)
            maximum = int(i)
        elif int(i) < minimum:
            minimum = int(i)
        elif int(i) > maximum:
            maximum = int(i)
        c += 1

main ()
