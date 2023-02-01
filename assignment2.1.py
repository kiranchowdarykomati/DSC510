# DSC 510
# Week 2
# Programming Assignment 2.1 Week 2
# Author Kiran Komati
# 12/11/2020
# Description: This program takes company name and no. of square feet and

# Change#:1
# Change(s) Made: Added error handling to check for invalid input lines 20-23 added
# Date of Change: 12/12/2020
# Author: Kiran Komati
# Change Approved by: Kiran Komati
# Date Moved to Production: 12/12/2020


import sys

print("\t\t\t\t\t\tWelcome to Bellevue Fiber Optics Cable Company.\n")
Company = input("Enter your Company name: ")

try:
    Feet = float(input("Enter the no. of feet of the fiber cable to be installed: "))
# Exception check if Feet entered is not a float
except ValueError:
    sys.exit("Enter a valid number")

if Feet <= 0:
    # Exit if Feet entered is less than zero
    sys.exit("Enter a valid length")
else:
    # Total=no. of feet times $0.87 and rounding it to two digits after decimal point
    TotalCost = round(Feet * 0.87, 2)
    print("\nPrinting receipt. Please be patient!!\n\n")
    print("Name of the Company:", Company)
    print("No. of feet of fiber to be installed:", Feet)
    print("Cost per foot: $0.87")
    print("Final cost: $"+str(TotalCost))
    print("\nHave a good day!!")
