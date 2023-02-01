# DSC 510
# Week 9
# Programming Assignment 9.1 Week 9
# Author Kiran Komati
# 02/14/2021
# Description: This program performs three essential operations. It will process Gettysburg.txt.
# Calculate the total words, and output the number of occurrences of each word in the file and
# write into an output file.

# Change#: 0
# Change(s) Made:
# Date of Change:
# Author:
# Date Moved to Production:


import sys
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


def process_file(wc_dictionary, file_name):
    value_key_list = []
    for key, val in wc_dictionary.items():
        value_key_list.append((val, key))
    # sorting in the reverse order
    value_key_list.sort(reverse=True)
    try:
        with open(file_name+'.txt', 'a') as new_file:
            new_file.write('{:15s}{:15s}'.format("word", "count")+"\n")
            new_file.write("\n")
            for val, key in value_key_list:
                new_file.write('{:16s}{:<3d}'.format(key, val)+"\n")
    except Exception as e:
        print(e)


def main():
    file_name = input("Enter the output file name(without extension): ")
    wc_dictionary = {}
    with open('gettysburg.txt', 'r') as getty_file:
        for line in getty_file:
            process_line(line, wc_dictionary)
        try:
            with open(file_name+'.txt', 'w') as new_file:
                new_file.write("Length of Dictionary: {}" .format(len(wc_dictionary))+"\n")
        except Exception as e:
            print(e)
            sys.exit("enter a valid file name")
        process_file(wc_dictionary, file_name)


if __name__ == "__main__":
    main()
