# DSC 510
# Week 11
# Programming Assignment 11.1 Week 11
# Author Kiran Komati
# 02/28/2021
# Description: This is a simple Cash Register Program

# Change#: 0
# Change(s) Made:
# Date of Change:
# Author:
# Date Moved to Production:

import sys
import locale


class CashRegister:

    def __init__(self):
        self.count = 0
        self.total = 0.0

    def addItem(self, price):
        # Add items to the list and increase the count
        if price == 0.0:
            pass
        else:
            self.count = self.count+1
            self.total = self.total + price

    def getTotal(self):
        # Get the total cost of items
        return self.total

    def getCount(self):
        # Get the total number of items
        return self.count

    def clearCart(self):
        # Clears the Cart
        self.count = 0
        self.total = 0.0


def main():
    locale.setlocale(locale.LC_ALL, 'English_United States.1252')
    print("Welcome to 'The Bellevue' General Store\n")
    CR = CashRegister()
    try:
        while True:
            print("Please enter the price to add an item to your cart, or 'exit' to exit. 'empty' will clear your cart")
            price = input("Price(in $): ")
            if price.lower() == 'exit':
                break
            elif price.lower() == 'empty':
                CR.clearCart()
            else:
                try:
                    floatprice = float(price)
                    CR.addItem(floatprice)
                except ValueError:
                    sys.exit("Invalid Price entered!")
            Total = CR.getTotal()
            TotalCostinUSD = locale.currency(Total, grouping=True)
            print("\nNo. of items in the cart: {}".format(CR.getCount()))
            print("Total Amount of items in the cart: "+TotalCostinUSD+"\n")
        print("\n\nHave a good rest of the day!")
    except Exception as E:
        print(E)


if __name__ == "__main__":
    main()
