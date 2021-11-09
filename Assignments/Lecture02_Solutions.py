"""
Solution to the exercise from lecture02
Author: Ronald Wedema
Date: 01-09-2017
"""

# ask user to input a dna sequence
dna_sequence = input("Please provide a DNA sequence: ")
# create a dictionary to hold the complement bases
complement_dict = {"A":"T", "T":"A", "C":"G", "G":"C"}

print(dna_sequence.upper())

# reverse the sequence
reverse_dna = dna_sequence[::-1]
print(reverse_dna.upper())

# create empty list to hold the complement bases
complement_dna_list = []

# loop over each base in the reversed dna sequence
for base in reverse_dna:
    # get the complement base from the dict
    complement_base = complement_dict[base]

    # add the complement base to the list
    complement_dna_list.append(complement_base)

# join elements from list (stringify) using tghe str.join() method
stringified_complement_dna_sequence = ''.join(complement_dna_list)

# print the result
print('complement dna sequence: ', stringified_complement_dna_sequence)


