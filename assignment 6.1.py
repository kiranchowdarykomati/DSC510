# DSC 510
# Week 6
# Programming Assignment 6.1 Week 6
# Author Kiran Komati
# 01/23/2021
# Description: This program takes different temperatures from user and prints the total no. of temperatures
# and the highest and lowest temperatures from the list

# Change#: 1
# Change(s) Made: Removed max() and min() for calculation and used for loop
# Date of Change: 01/24/2021
# Author: Kiran Komati
# Date Moved to Production:


import sys


def main():
    print("This program allows the user to add temperatures to a list\n")
    print("Enter temperatures. Press 'q' to Quit\n")
    ReadytoQuit = ''
    temperatures = []
    while ReadytoQuit.lower() != 'q':
        enteredvalue = input("")
        if enteredvalue == 'q':
            break
        else:
            try:
                enteredValuefloat = float(enteredvalue)
                if not isinstance(enteredValuefloat, float):
                    sys.exit("Invalid input!!")
                else:
                    temperatures.append(enteredValuefloat)
            except ValueError:
                sys.exit("Invalid input!!")
    # Assign first number in the list as default smallest and largest numbers

    smallest = temperatures[0]
    largest = temperatures[0]

    for i in range(1, len(temperatures)):
        # if the iterated value is less than smallest number then make iterated value as smallest
        if temperatures[i] < smallest:
            smallest = temperatures[i]
        # if the iterated value is greater than largest number then make iterated value as largest
        elif temperatures[i] > largest:
            largest = temperatures[i]
        else:
            continue
    print("\nTotal no. of temperatures in the list: ", len(temperatures))
    print("The largest temperature in the list: ", largest)
    print("The smallest temperature in the list: ", smallest)
    print("\nThank you for using the application. Have a good day!")


if __name__ == "__main__":
    main()
