# DSC 510
# Week 10
# Programming Assignment 10.1 Week 10
# Author Kiran Komati
# 02/20/2021
# Description: This program uses request library to get Chuck Norris jokes and display on the screen.
# This requests as many jokes as the user wants based on the key strokes entered.

# Change#: 0
# Change(s) Made:
# Date of Change:
# Author:
# Date Moved to Production:


import requests


def main():
    print("Welcome to Chuck Norris Jokes\n")
    proceed = 'y'
    try:
        proceed = input("Do you want to request a Chuck Norris joke today? Enter 'y' for yes and any other key to Quit: ")
        while proceed.lower() == 'y':
            response = requests.get("https://api.chucknorris.io/jokes/random")
            joke_dictionary = response.json()
            print(joke_dictionary)
            joke = joke_dictionary["value"]
            print(joke)
            proceed = input("\nEnter 'y' for next joke or any other key to exit: ")
        print("\n\nThat's all for today!")
    except Exception as E:
        print(E)


if __name__ == "__main__":
    main()
