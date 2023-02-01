# DSC 510
# Week 8
# Programming Assignment 8.1 Week 8
# Author Kiran Komati
# 02/07/2021
# Description: This program performs three essential operations. It will process Gettysburg.txt.
# Calculate the total words, and output the number of occurrences of each word in the file.

# Change#: 0
# Change(s) Made:
# Date of Change:
# Author:
# Date Moved to Production:


import string


def process_line(line, wc_dictionary):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            # Adding Keys to the dictionary
            add_word(word, wc_dictionary)


def add_word(word, wc_dictionary):
    # if word is already present, increase the count value by one otherwise assign 1 to count
    if word in wc_dictionary:
        wc_dictionary[word] += 1
    else:
        wc_dictionary[word] = 1


def pretty_print(wc_dictionary):
    value_key_list = []
    for key, val in wc_dictionary.items():
        value_key_list.append((val, key))
    # sorting in the reverse order
    value_key_list.sort(reverse=True)
    print('{:15s}{:15s}'.format("word", "count"))
    print(''*50)
    for val, key in value_key_list:
        print('{:16s}{:<3d}'.format(key, val))


def main():
    wc_dictionary = {}
    try:
        getty_file = open('gettysburg.txt', 'r')
    except FileNotFoundError as e:
        print(e)
    for line in getty_file:
        process_line(line, wc_dictionary)
    print("Length of Dictionary:", len(wc_dictionary))
    pretty_print(wc_dictionary)


if __name__ == "__main__":
    main()
