"""
Solution to the exercise from lecture03
Author: Ronald Wedema
Date: 01-09-2017
"""

# import all functions from the rev_comp module
from rev_comp import *


def main(): 
    # call the functions in the correct order, catching the returned values
    dna_sequence_from_user = ask_input()
    # pass the catched value to the next function as its argument and store the returned value
    reverse_dna = reverse_dna_sequence(dna_sequence_from_user)
    # pass the catched value to the next function as its argument and store the returned value
    reverse_complement_dna = create_complement_dna(reverse_dna)

    # print the final result
    print("reverse complemented dna: ", reverse_complement_dna)

# check if this is the main running module
if __name__ == '__main__':
    main()
