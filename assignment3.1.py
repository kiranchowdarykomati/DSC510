# DSC 510
# Week 3
# Programming Assignment 3.1 Week 3
# Author Kiran Komati
# 12/11/2020
# Description: This program takes company name and no. of square feet and provides discount based
#              on the no. of feet entered.

# Change#:1
# Change(s) Made: Added conditional execution to provide discount
# Date of Change: 12/19/2020
# Author: Kiran Komati
# Change Approved by: Kiran Komati
# Date Moved to Production: 12/19/2020


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
    # If it's more than 100 feet and less than or equal to 250 charge $0.80 per foot
elif 100 < Feet <= 250:
    CostPerFeet = 0.80
    # If it's more than 250 feet and less than or equal to 500 charge $0.70 per foot
elif 250 < Feet <= 500:
    CostPerFeet = 0.70
    # If it's more than 500 feet charge $0.50 per foot
elif Feet > 500:
    CostPerFeet = 0.50
    # Default charge $0.87 per foot
else:
    CostPerFeet = 0.87
    # Total = no. of feet times $0.87 and rounding it to two digits after decimal point
TotalCost = round(Feet * CostPerFeet, 2)

print("\nPrinting receipt. Please be patient!!\n\n")
print("Name of the Company: ", Company)
print("No. of feet of fiber to be installed: ", Feet)
print("Cost per foot: ", CostPerFeet)
print("Final cost: $"+str(TotalCost))
print("\nHave a good day!!")
