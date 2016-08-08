#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def print_large_words():
    try:
        with open("words.txt", "r") as file_object:
            contents = file_object.read()
            contents = contents.split("\n")
            for word in contents:
                if len(word) > 20:
                    print(word)
    except:
        print("Sorry, problem with reading the file. Check if file is present in your working directory.")

##############################################################################
def main():
    print_large_words()

if __name__ == '__main__':
    main()
