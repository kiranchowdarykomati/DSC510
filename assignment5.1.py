# DSC 510
# Week 5
# Programming Assignment 5.1 Week 5
# Author Kiran Komati
# 01/16/2021
# Description: This program takes company name and no. of square feet and provides discount based
#              on the no. of feet entered.

# Change#:
# Change(s) Made:
# Date of Change:
# Author:
# Date Moved to Production:

# The program will perform various math operations based on the input from user
# 1 to add, 2 to subtract, 3 to multiply, 4 to divide, or 5 for average


import sys


def performCalculation(operation):
    try:
        first = float(input("\nenter the first number: "))
        second = float(input("enter the second number: "))
    # Exception check to verify if the number entered is not a float
    except ValueError:
        sys.exit("Enter a valid number")
    result = 0.0
    if operation == 1:
        result = first + second
    elif operation == 2:
        result = first - second
    elif operation == 3:
        result = first * second
    elif operation == 4:
        result = first / second
    print("the result is :", result)


def calculateAverage():
    try:
        count = int(input("\nHow many numbers do you want to enter: "))
        total = 0
        for x in range(count):
            number = float(input("enter a number: "))
            total = total + number
        average = total / count
        print("The average is: ", average)
    # Exception check to verify if the number entered is not a float
    except ValueError:
        sys.exit("Enter a valid number")


def main():
    print("This program allows the user to perform different math operations")
    proceed = 'y'
    try:
        while proceed.lower() == 'y':
            print("\nWould you like to add, subtract, multiply, divide, or calculate Average? ")
            operation = int(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, or 5 for average: "))
            # Validate if the operation is less than or equal to 4
            if 0 < operation <= 4:
                performCalculation(operation)
            elif operation == 5:
                calculateAverage()
            else:
                print("enter a valid number to perform the operation.")
            proceed = input("\nEnter 'y' to continue or any other character to exit: ")
        print("\nThank you for using the application. Have a good day!")
    except ValueError:
        sys.exit("Invalid input!!")


if __name__ == "__main__":
    main()
