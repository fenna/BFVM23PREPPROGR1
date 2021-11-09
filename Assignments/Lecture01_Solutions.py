"""
Solution to the exercise from lecture01
Author: Ronald Wedema
Date: 01-09-2017
"""

# define variables
unknown_sequence = "ATGAGTAGGATAGGCTAGGATGGCGATGAATT"
is_dna = True
base_letters = "ACTG"

# loop over the sequence, each time taking a single base
for letter in unknown_sequence:
    if letter != "A" and letter != "T" and letter != "C" and letter != "G":
    # alternatively you can use the in keyword to check if the letter is part of other Python datatypes
    # if letter not in base_letters:
        # if the above condition is true, set the boolean to false
        is_dna = False

# do we have a dna sequence?
if is_dna:
    # reverse the sequence
    dna_reversed = unknown_sequence[::-1]
    # replace T with U, to create a rna sequence
    rna = dna_reversed.replace("T", "U")
    print("DNA reversed sequence: ", dna_reversed)
    print("RNA seqeunce: ", rna)
