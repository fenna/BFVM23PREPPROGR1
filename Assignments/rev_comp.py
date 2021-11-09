"""
Solution to the exercise from lecture03
This module contains the 3 functions that should be imported into Lecture03_Solution.py
Author: Ronald Wedema
Date: 01-09-2017
"""

def ask_input():
    """
    Function to ask input from a user

    : return string with user input
    """
    asked_input = input("Please provide a DNA sequene: ")

    return asked_input


def reverse_dna_sequence(seq):
    """
    Function that reverses a given sequence

    : param seq a string sequence
    : return reversed_dna string with reversed sequence
    """

    reversed_dna = seq[::-1]

    return reversed_dna


def create_complement_dna(dna):
    """
    Function that will create a complement sequence

    : param dna string holding a dna sequence
    : return complement_dna string holding the complement dna sequence
    """

    complement_dna = ""
    complement_dict = {"A":"T", "T":"A", "C":"G", "G":"C"}

    # loop over each base in the reversed dna sequence
    for base in dna:
    # get the complement base from the dict and add to the complement_dna string
        complement_dna += complement_dict[base]

    return complement_dna


def main():
    # normally you would run the functions from this module inside the main
    pass

# check if this is the main running module
if __name__ == '__main__':
    main()
