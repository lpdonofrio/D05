#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def read_long_words():
    try:
        fin = open("words.txt")
    except:
        print("File did not open")
    for line in fin:
        #Question: how does python know what the element to analyze is?
        #I haven't defined line = fin.readline() or anything like that
        #The same happens in something like:
        #   for letter in word:
        #       if letter ....bla bla
        word = line.strip()
        if len(word) > 20:
            print(word)

##############################################################################
def main():

    read_long_words()

if __name__ == '__main__':
    main()
