# DSC 510
# Week 4
# Programming Assignment 4.1 Week 4
# Author Kiran Komati
# 12/11/2020
# Description: This program takes company name and no. of square feet and provides discount based
#              on the no. of feet entered.

# Change#:2
# Change(s) Made: Added function
# Date of Change: 01/09/2021
# Author: Kiran Komati
# Change Approved by: Kiran Komati
# Date Moved to Production: 01/09/2021


import sys
import locale


def costcalculator(feet, costperfeet):
    # Total = no. of feet times costperfeet and rounding it to two digits after decimal point
    totalcost = round(feet * costperfeet, 2)
    return totalcost


print("\t\t\t\t\t\tWelcome to Bellevue Fiber Optics Cable Company.\n")
Company = input("Enter your Company name: ")

try:
    TotalFeet = float(input("Enter the no. of feet of the fiber cable to be installed: "))
# Exception check if Feet entered is not a float
except ValueError:
    sys.exit("Enter a valid number")

locale.setlocale(locale.LC_ALL, 'English_United States.1252')

if TotalFeet <= 0:
    # Exit if Feet entered is less than zero
    sys.exit("Enter a valid length")

    # If it's more than 100 feet and less than or equal to 250 charge $0.80 per foot
elif 100 < TotalFeet <= 250:
    TotalCost = costcalculator(TotalFeet, 0.80)
    # If it's more than 250 feet and less than or equal to 500 charge $0.70 per foot
elif 250 < TotalFeet <= 500:
    TotalCost = costcalculator(TotalFeet, 0.70)
    # If it's more than 500 feet charge $0.50 per foot
elif TotalFeet > 500:
    TotalCost = costcalculator(TotalFeet, 0.50)
    # Default charge $0.87 per foot
else:
    TotalCost = costcalculator(TotalFeet, 0.87)

# Convert Total Cost to USD
TotalCostinUSD = locale.currency(TotalCost, grouping=True)

print("\nPrinting receipt. Please be patient!!\n\n")
print("Name of the Company: ", Company)
print("No. of feet of fiber to be installed: ", TotalFeet)
print("Final cost: " + TotalCostinUSD)
print("\nHave a good day!!")
